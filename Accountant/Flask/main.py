from flask import Flask, redirect, url_for, render_template, request
from run_accountant import Accountant
from flask_sqlalchemy import SQLAlchemy


accountant = Accountant()


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String(100))
    amount = db.Column(db.Integer)
    comment = db.Column(db.String(100))
    product_name = db.Column(db.String(100))
    product_price = db.Column(db.Integer)
    product_qty = db.Column(db.Integer)


@accountant.add('from_db')
def open(accountant, *args):
    database = args[0]
    rows = database.query.all()
    columns = database.__table__.columns.keys()

    for row in rows:
        history_dict = {}
        for col in columns:
            history_dict[col] = getattr(row, col)
        action = history_dict['action']
        if action == 'saldo':
            amount = history_dict['amount']
            accountant.balance += int(amount)
        elif action == 'zakup':
            product_name = history_dict['product_name']
            product_price = history_dict['product_price']
            product_qty = history_dict['product_qty']
            accountant.balance -= int(product_price) * int(product_qty)
            if product_name in accountant.warehouse:
                accountant.warehouse[product_name] += int(product_qty)
            else:
                accountant.warehouse[product_name] = int(product_qty)
        elif action == 'sprzedaz':
            product_name = history_dict['product_name']
            product_price = history_dict['product_price']
            product_qty = history_dict['product_qty']
            accountant.balance += int(product_price) * int(product_qty)
            accountant.warehouse[product_name] -= int(product_qty)
            if accountant.warehouse[product_name] == 0:
                del accountant.warehouse[product_name]
        else:
            continue

@accountant.add('save_db')
def save(accountant, *args):
    database = args[0]
    action = args[1]
    if action == 'saldo':
        amount, comment = args[2:]
        entry = Data(action=action, amount=amount, comment=comment)
    else:
        product_name, product_price, product_qty = args[2:]
        entry = Data(action=action, product_name=product_name,
                     product_price=product_price, product_qty=product_qty)
    database.session.add(entry)
    database.session.commit()

@accountant.add('saldo')
def add(accountant, *args):
    ammount, comment = args
    accountant.balance += ammount
    accountant.run('save_db', db, 'saldo', ammount, comment)

@accountant.add('zakup')
def add(accountant, *args):
    product_name, product_price, product_qty = args
    if accountant.balance >= int(product_price) * int(product_qty):
        accountant.balance -= int(product_price) * int(product_qty)
        if product_name in accountant.warehouse:
            accountant.warehouse[product_name] += int(product_qty)
        else:
            accountant.warehouse[product_name] = int(product_qty)
        accountant.run('save_db', db, 'zakup', product_name,
                  product_price, product_qty)

@accountant.add('sprzedaz')
def add(accountant, *args):
    product_name, product_price, product_qty = args
    if product_name in accountant.warehouse:
        if accountant.warehouse[product_name] >= product_qty:
            accountant.balance += int(product_price) * int(product_qty)
            accountant.warehouse[product_name] -= int(product_qty)
            if accountant.warehouse[product_name] == 0:
                del accountant.warehouse[product_name]
            accountant.run('save_db', db, 'sprzedaz', product_name,
                  product_price, product_qty)

@app.route('/')
def home():
     return render_template('index.html', balance=accountant.balance, warehouse=accountant.warehouse)

@app.route('/', methods=['POST'])
def up():
    if request.form['submit'] == 'saldo':
        amount = int(request.form['amount'])
        comment = request.form['comment']
        accountant.run('saldo', amount, comment)
    elif request.form['submit'] == 'zakup':
        product_name = request.form['name']
        product_price = request.form['price']
        product_qty = request.form['qty']
        accountant.run('zakup', product_name, product_price, product_qty)
    elif request.form['submit'] == 'sprzedaz':
        product_name = request.form['name']
        product_price = int(request.form['price'])
        product_qty = int(request.form['qty'])
        accountant.run('sprzedaz', product_name, product_price, product_qty)
    elif request.form['submit'] == 'history':
        return redirect(url_for('history', line_from=1, line_to=len(Data.query.all())))
    return redirect(url_for('home'))


@app.route('/history/<line_from>/<line_to>/')
def history(line_from, line_to):
    line_from, line_to = int(line_from), int(line_to)
    if line_from < 1:
        line_from = 1
    if line_to > len(Data.query.all()):
        line_to = len(Data.query.all())
    if line_from > line_to:
        line_from, line_to = line_to, line_from
    new_range = range(int(line_from), int(line_to)+1)
    rows = Data.query.filter(Data.id.in_(new_range)).all()
    columns = Data.__table__.columns.keys()

    history_table = []

    for row in rows:
        history_dict = {}
        for col in columns:
            atr = getattr(row, col)
            if atr != None:
                history_dict[col] = atr
        history_table.append(str(history_dict).replace("{","").replace("}","").replace("'",""))
    return render_template('history.html', history=history_table, max_value=len(Data.query.all()))


@app.route('/history/<line_from>/<line_to>/', methods=['POST'])
def historyRange(line_from, line_to):
    line_from = request.form['history_line_from']
    line_to = request.form['history_line_to']
    if line_from == "":
        line_from = 1
    if line_to == "":
        line_to = len(Data.query.all())
    return redirect(url_for('history', line_from=line_from, line_to=line_to))


db.create_all()
accountant.run('loadFromDatabase', Data)
