from datetime import date

# If today is Monday (aka 0 of 6), then run the report
if date.today().weekday() == 0:
    print("mon")
if date.today().weekday() == 1:
    print("tue")
if date.today().weekday() == 2:
    print("wed")
if date.today().weekday() == 3:
    print("th")
if date.today().weekday() == 4:
    print("fri")
if date.today().weekday() == 5:
    print("sat")
if date.today().weekday() == 6:
    print("sun")
