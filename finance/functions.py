from typing import Any


def flt_to_money(money_flt: float, pad: int = 0) -> str:
    """ Convert float to formatted string with option to right pad"""
    return f"{money_flt:>{pad},.2f}"


def list_to_money(money_items: Any, pad: int = 0, sep: str = ' ') -> str:
    """ Convert multiple floats to formatted string with optional right padding and seperator"""
    return sep.join([f"{flt_to_money(money_item, pad)}" for money_item in money_items])


def list_to_string(string_list: Any, pad: int = 0, sep: str = ' ') -> str:
    """ Right justify tuple to length of longest string element. """
    return sep.join([list_string.rjust(pad) for list_string in string_list])


def get_longest_string(strings: Any) -> int:
    """ get longest string length from iterable. """
    string_list = sorted(strings, key=len, reverse=True)
    return len(string_list[0])

def month_reached(range_months: int, month: int) -> bool:
    """ True if month reached target. """
    month_bool: bool = False
    if range_months is None:
        pass
    elif month >= range_months > 0:
        month_bool = True
    return month_bool


def amount_reached(initial_amount: float, target_amount: float, amount: float) -> bool:
    """ True if the amounts have reached target. """
    amount_bool: bool = False
    if target_amount is None:
        pass
    elif initial_amount <= target_amount <= amount:
        amount_bool = True
    elif initial_amount >= target_amount >= amount:
        amount_bool = True
    return amount_bool


def monthly_projection_data(
        interest_rate: float,
        monthly_transaction: float,
        initial_amount: float,
        month_span: int ,
        target_amount: float,
) -> list:
    """ Provide annual projection of savings based on monthly saving amount.
        This version produces data in list of dictionaries.
     """
    finance_data: list = []
    interest_month_rate = (interest_rate / 100) / 12
    total_interest = 0.0
    total_amount: float = initial_amount
    month_range: int
    month: int = 0
    running: bool = True
    #If neither of the parameters are set then assign a default to run annual timeframe
    if month_span is None and target_amount is None:
        month_range = 12
    else:
        month_range = month_span

    while running:
        month += 1
        interest_month = interest_month_rate * total_amount
        total_interest += interest_month
        total_amount += interest_month + monthly_transaction
        added_value = total_amount - initial_amount
        savings = {'Month': month, 'Interest Added': interest_month, 'Interest Total': total_interest,
                   'Amount Added': added_value, 'Amount Total': total_amount}
        finance_data.append(savings)
        if month_reached(month_range, month):
            running = False
        if amount_reached(initial_amount, target_amount, total_amount):
            running = False
    return finance_data





def inputs_to_dict(
    interest_rate: float = 0,
    monthly_transaction: float = 0,
    initial_amount: float = 0,
    month_span: int = None,
    target_amount: float =None,
    )-> dict:
    """ Take individual parameters and convert into dictionary. """
    input_dict:dict = {interest_rate: interest_rate,monthly_transaction: monthly_transaction
        , initial_amount: initial_amount,month_span: month_span,target_amount: target_amount }
    return input_dict




def monthly_projection_text(
        interest_rate: float = 0,
        monthly_transaction: float = 0,
        initial_amount: float = 0,
        month_span: int = None,
        target_amount: float =None,
) -> str:
    """ Provide annual projection of savings based on monthly saving amount.
           This version produces data as formatted string.
        """
    report = monthly_projection_data(interest_rate, monthly_transaction, initial_amount, month_span, target_amount)
    report_keys = report[0].keys()
    pad_len = get_longest_string(report_keys)
    sep: str = '|'
    report_headers = list_to_string(report[0].keys(), pad_len, sep).title()
    report_text: str = report_headers
    for row in report:
        report_text += (
            f"\n{row['Month']:>{pad_len}}{sep}{list_to_money(
                (row['Interest Added']
                 , row['Interest Total']
                 , row['Amount Added']
                 , row['Amount Total'])
                , pad_len, sep)}")
    return report_text
