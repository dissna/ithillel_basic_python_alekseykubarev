def is_even(number):
    return even if number % 2 == 0 else odd


even = 'even'
odd = 'odd'
number = int(input("Enter the number: "))
print("The entered number is {}".format(is_even(number)))