year =  int(input("Type the year: "))
# The year the gregorian calendar was created.
gregorian_calendar = 1582

if year % 4 != 0 and year > gregorian_calendar:
    print("Commum year")
elif year % 100 != 0 and year > gregorian_calendar:
    print("Leap year")
elif year % 400 != 0 and year > gregorian_calendar:
    print("Commum year")
elif year < gregorian_calendar:
    print("This year is no in the gregorian calendar")
else:
    print("Leap year")