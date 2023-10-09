from flask import Flask, render_template, request, redirect, url_for
from acc import Acc


file_path = "acc.txt"
a = Acc()
a.open(file_path)


# ZAPISYWANIE DO PLIKU

@a.add('saldo')
def add(a, *args):
    amount, comment = args
    a.balance += amount
    a.save(file_path, f'saldo {amount} {comment}')

@a.add('zakup')
def add(a, *args):
    product_name, product_price, product_qty = args
    if a.balance >= int(product_qty) * int(product_price):
        a.balance -= int(product_qty) * int(product_price)
        if product_name in a.warehouse:
            a.warehouse[product_name] += int(product_qty)
        else:
            a.warehouse[product_name] = int(product_qty)
        a.save(file_path, f'zakup {product_name} {product_price} {product_qty}')

@a.add('sprzedaz')
def add(a, *args):
    product_name, product_price, product_qty = args
    if product_name in a.warehouse:
        if a.warehouse[product_name] >= product_qty:
            a.balance += int(product_price) * int(product_qty)
            a.warehouse[product_name] -= int(product_qty)
            if a.warehouse[product_name] == 0:
                del a.warehouse[product_name]
            a.save(file_path, f'sprzedaz {product_name} {product_price} {product_qty}')


app = Flask(__name__)


@app.route('/')
def home():
     return render_template("index.html", balance=a.balance, warehouse=a.warehouse)


@app.route('/', methods=['POST'])
def up():
    if request.form['submit'] == 'saldo':
        amount = int(request.form["amount"])
        comment = request.form["comment"]
        a.run("saldo", amount, comment)
    elif request.form['submit'] == 'zakup':
        product_name = request.form['name']
        product_price = request.form['price']
        product_qty = request.form['qty']
        a.run('zakup', product_name, product_price, product_qty)
    elif request.form["submit"] == "sprzedaz":
        product_name = request.form['name']
        product_price = int(request.form['price'])
        product_qty = int(request.form['qty'])
        a.run("sprzedaz", product_name, product_price, product_qty)
    elif request.form["submit"] == "history":
        return redirect(url_for("history", line_from=1, line_to=len(open(file_path).readlines())))
    return redirect(url_for('home'))


@app.route("/history/<line_from>/<line_to>/")
def history(line_from, line_to):
    line_from, line_to = int(line_from), int(line_to)
    if line_from < 1:
        line_from = 1
    if line_to > len(open(file_path).readlines()):
        line_to = len(open(file_path).readlines())
    if line_from > line_to:
        line_from, line_to = line_to, line_from
    return render_template("history.html", history=open(file_path).readlines()[line_from-1:line_to])

@app.route("/history/<line_from>/<line_to>/", methods=["POST"])
def historyRange(line_from, line_to):
    line_from = request.form["history_line_from"]
    line_to = request.form["history_line_to"]
    if line_from == "":
        line_from = 1
    if line_to == "":
        line_to = len(open(file_path).readlines())
    return redirect(url_for("history", line_from=line_from, line_to=line_to))


