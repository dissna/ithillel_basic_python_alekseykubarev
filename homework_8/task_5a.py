from random import randint

def get_max_digit(number):
    largest = 0
    while (number):
        a = number % 10
        largest = max(a, largest)
        number = number // 10
    return largest


number = randint(100000000000, 999999999999)
print('A 12-digit natural number: ', number)
print('Maximum digit of a natural number: ',get_max_digit(number))