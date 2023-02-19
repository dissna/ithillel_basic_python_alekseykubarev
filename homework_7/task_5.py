import random

print("The program chose a number from 1 to 10, guess it:")
n = int(input("Enter your number: "))
a = random.randint(1,10)
while n!=a:
    if n < a:
        print("Your number is less.")
    if n > a:
        print("Your number is greater.")
    if n==a:
        print("You guessed!")
    n = int(input("Enter your number: "))

print("You guessed!")