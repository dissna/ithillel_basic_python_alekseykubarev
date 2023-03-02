import random

def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Будь ласка, введіть ціле число.")
            continue
        else:
            return value

def get_str(prompt):
    while True:
        value = input(prompt).strip()
        if len(value) == 0:
            print("Будь ласка, введіть текст.")
            continue
        else:
            return value

def generate_random_number():
    return random.randint(1, 100)

def guess_number():
    number = generate_random_number()
    while True:
        guess = get_integer("Введіть число від 1 до 100: ")
        if guess == number:
            print("Вітаємо! Ви вгадали число!")
            break
        elif guess < number:
            print("Загадане число більше.")
        else:
            print("Загадане число менше.")

def program_guess():
    min_number = 1
    max_number = 100
    while True:
        guess = (min_number + max_number) // 2
        answer = get_str(f"Чи це число {guess}? Введіть 'більше', 'менше' або 'вірно': ")
        if answer == 'вірно':
            print("Програма вгадала число!")
            break
        elif answer == 'більше':
            min_number = guess + 1
        elif answer == 'менше':
            max_number = guess - 1
        else:
            print("Будь ласка, введіть 'більше', 'менше' або 'вірно'.")

def main():
    while True:
        game_choice = get_str("Оберіть гру: '1' - вгадати число, '2' - вгадування програмою, 'exit' - завершити гру: ")
        if game_choice == '1':
            guess_number()
        elif game_choice == '2':
            program_guess()
        elif game_choice == 'exit':
            print("Дякую за гру!")
            break
        else:
            print("Будь ласка, введіть '1', '2' або 'exit'.")

if __name__ == '__main__':
    main()