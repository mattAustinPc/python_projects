from typing import Any
from functions import monthly_projection_text
interest_rate = 4.0
month_amount = 200
initial_amount = 2000.00
range_months =  None
target_amount = 140000

#report_text = monthly_projection_text(interest_rate, month_amount,initial_amount,range_months,target_amount)
#print('Version as formatted text..........\n')
#print(report_text)


def iter_power(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    result = 1
    count = exp
    while count > 0:
        result *= base
        count -= 1
    return result


def recur_power(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 1:
        return base
    else:
        return recur_power(base, exp - 1)* base

print(iter_power(4, 3))
print(recur_power(4, 3))