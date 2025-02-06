from functions import saving_annual_summary
month_amount = 100
interest_rate = 4.01
saving_report = saving_annual_summary(month_amount,interest_rate,0)
print(f"A monthly saving of £{month_amount}, with annual interest of {interest_rate}%"
      f" will produce a saving of:\n{saving_report}")
