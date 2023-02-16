def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        result = True
    elif year % 400 == 0:
        result = True
    else:
        result = False
    return result


year = int(input("Enter year: "))
print("This year is a leap year:", leap_year(year))