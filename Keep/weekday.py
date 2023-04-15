#this program outputs whether or not today is a weekday

#Author: Emma Dunleavy

import calendar

from datetime import date

today=date.today()

print ("today's date is:", today)

#ref https://www.programiz.com/python-programming/datetime/current-datetime

x_date = calendar.day_name.weekday()
no = x_date.weekday()

if no < 5:
    print("Date is weekday")
else: #5 Sat, 6 Sun
    print("Date is weekend")

#ref https://pynative.com/python-get-the-day-of-week/
