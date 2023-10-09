import sys
from main import zmienna


amount = sys.argv[2]
comment = sys.argv[3]
zmienna.change_balance(amount, comment)
