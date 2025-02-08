from typing import Any

def money(money_flt: float, pad: int = 0) -> str:
    """ Convert float to formatted string with option to right pad"""
    return f"{money_flt:>{pad},.2f}"

def money_list(money_items: Any, pad: int = 0, sep :str = "," ) -> str:
    """ Convert multiple floats to formatted string with optional right padding and seperator"""
    return sep.join([f"{money(money_item,pad)}" for money_item in money_items])

def get_longest_string(strings: tuple)->int:
    """ get longest string length from iterable. """
    string_list = sorted(strings,key=len, reverse=True)
    return len(string_list[0])

def rpad_tup(tup: tuple,pad: int)->tuple:
    """ Right justify tuple to length of longest string element. """
    return tuple([tup_string.rjust(pad) for tup_string in tup])

def monthly_interest_report(
        interest_rate: float,
        monthly_transaction: float=0,
        initial_amount: float = 0,
        months: int = 12,
        ) -> list:
    """ Provide annual projection of savings based on monthly saving amount. """
    interest_report: list = []
    interest_month_rate = (interest_rate / 100) / 12
    total_interest = 0.0
    total_value: float = round(initial_amount,2)
    for month in range(1,months+1):
        interest_month = round(interest_month_rate * total_value,2)
        total_interest += interest_month
        total_value = round(interest_month + monthly_transaction + total_value,2)
        added_value =  round(total_value-initial_amount,2)
        savings = dict(month=month, added_interest=interest_month, total_interest=total_interest,added_value= added_value,
                       total_value=total_value)
        interest_report.append(savings)
    return interest_report