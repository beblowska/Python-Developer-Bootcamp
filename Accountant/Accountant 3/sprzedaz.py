import sys
from main import zmienna

product_name = sys.argv[1]
product_price = sys.argv[2]
product_qty = sys.argv[3]
zmienna.sell(product_name, product_price, product_qty)
