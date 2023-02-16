def is_even(number):
    return True if number % 2 == 0 else False


number = int(input("Enter the number: "))
print("The entered number is paired:", is_even(number))