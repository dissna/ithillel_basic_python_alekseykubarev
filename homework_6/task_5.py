def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        result = "This year is a leap year"
    elif year % 400 == 0:
        result = "This year is a leap year"
    else:
        result = "This year is not a leap year"
    return result


year = int(input("Enter year: "))
print(leap_year(year))