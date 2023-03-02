import string
import random


def generate_password(length):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    allowed_chars = uppercase_letters + lowercase_letters + digits + "_"

    if length < 8:
        length = 8

    password = ''
    while True:
        password = ''.join(random.choice(allowed_chars) for i in range(length))
        if (any(char.isupper() for char in password) and
                any(char.islower() for char in password) and
                any(char.isdigit() for char in password) and
                not any(password[i] == password[i + 1] == char for i, char in enumerate(password[:-2]))):
            break

    return password

def main():
    length = int(input("Вкажіть довжину пароля(8+): "))
    if length >= 8:
        print(f'Пароль довжиною {length} символів:', generate_password(length))
    else:
        print(f'Пароль довжиною 8 символів:', generate_password(length))

if __name__ == '__main__':
    main()