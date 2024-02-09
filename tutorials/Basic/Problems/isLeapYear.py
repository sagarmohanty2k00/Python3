_year = int(input("Year: "))

if (_year%100 == 0 and _year%400 == 0) or (_year%4 == 0 and _year%100 != 0):
    print(_year, " is a leap year")
else:
    print(_year, " is not a leap year")