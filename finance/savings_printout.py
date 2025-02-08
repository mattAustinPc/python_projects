from functions import monthly_interest_report

month_amount = 100
interest_rate = 4.01
saving = 30000
print(f"A monthly saving of £{month_amount:,.2f} on top of £{saving:,.2f}, with annual interest of {interest_rate}%"
      f" will produce savings of:\n")

report = monthly_interest_report(interest_rate, month_amount,interest_rate,12)

for item in report:
    print(item)