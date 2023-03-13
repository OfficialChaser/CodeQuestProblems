import sys
import math

NumberOfCases = int(sys.stdin.readline().strip())

for i in range(NumberOfCases):
    amount = sys.stdin.readline().strip()
    printamt = amount
    amount = amount.strip("$")
    amount = float(amount)
    print(printamt)

    quarters = math.floor(amount / 0.25)
    print(f'Quarters={quarters}')
    qua_amt = (quarters * 0.25)
    amount = round(amount - qua_amt, 2)

    dimes = math.floor(amount / 0.10)
    print(f'Dimes={dimes}')
    dim_amt = (dimes * 0.10)
    amount = round(amount - dim_amt, 2)

    nickels = math.floor(amount / 0.05)
    print(f'Nickels={nickels}')
    nick_amt = (nickels * 0.05)
    amount = round(amount - nick_amt, 2)

    pennies = math.floor(amount / 0.01)
    print(f'Pennies={pennies}')
    pen_amt = (pennies * 0.01)
    amount = round(amount - pen_amt, 2)