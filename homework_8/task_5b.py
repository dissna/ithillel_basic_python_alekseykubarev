from random import randint

def get_max_digit(number):
    max = number % 10
    number = number // 10
    while number > 0:
        if number % 10 > max:
            max = number % 10
        number = number // 10
    return max


number = randint(100000000000, 999999999999)
print('A 12-digit natural number: ', number)
print('Maximum digit of a natural number: ',get_max_digit(number))