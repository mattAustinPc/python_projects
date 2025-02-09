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


def month_interest_data(
        interest_rate: float,
        monthly_transaction: float = 0,
        initial_amount: float = 0,
        months: int = 12,
) -> list:
    """ Provide annual projection of savings based on monthly saving amount.
        This version produces data in list of dictionaries.
     """
    interest_data: list = []
    interest_month_rate = (interest_rate / 100) / 12
    total_interest = 0.0
    total_value: float = initial_amount
    for month in range(1, months + 1):
        interest_month = interest_month_rate * total_value
        total_interest += interest_month
        total_value += interest_month + monthly_transaction
        added_value = total_value - initial_amount
        savings = {'Month': month, 'Interest Added': interest_month, 'Interest Total': total_interest,
                   'Amount Added': added_value, 'Amount Total': total_value}
        #print(savings)
        interest_data.append(savings)
    return interest_data


def month_interest_text(
        interest_rate: float,
        monthly_transaction: float = 0,
        initial_amount: float = 0,
        months: int = 12,
) -> str:
    """ Provide annual projection of savings based on monthly saving amount.
           This version produces data as formatted string.
        """
    report = month_interest_data(interest_rate, monthly_transaction, initial_amount, months)
    report_keys = report[0].keys()
    pad_len = get_longest_string(report_keys)
    sep: str ='|'
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
