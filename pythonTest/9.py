"""Write a Python program that takes a date in YYYY-MM-DD format and returns the day of the
week (e.g., "Monday", "Tuesday")."""

import datetime

date_ip = input("Enter a date in YYYY-MM-DD format: ")
day_name = datetime.datetime.strptime(date_ip, '%Y-%m-%d').strftime('%A')

print(day_name)