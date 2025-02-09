from typing import Any
from functions import  month_interest_data, month_interest_text

month_amount = 50.00
interest_rate = 12.0
saving = 10000.00
report_data = month_interest_data(month_amount, interest_rate)
report_text = month_interest_text(interest_rate, month_amount, saving)


print('Version as formatted text..........\n')
print(report_text)

print('\nVersion as list of dictionaries.......................\n')
for row in report_data:
    print(row)