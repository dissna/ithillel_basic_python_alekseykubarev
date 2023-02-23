def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return leap
    elif year % 400 == 0:
        return leap
    else:
        return not_leap


leap = 'leap'
not_leap = 'not leap'
year = int(input("Enter year: "))
print("This is {} year".format(leap_year(year)))