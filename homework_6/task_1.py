def is_even(number):
    if number % 2 == 0:
        result = "Even"
    else :
        result = "odd"
    return result


number = int(input("Enter the number: "))
print("Your result is", is_even(number))