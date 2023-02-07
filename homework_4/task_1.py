text = input('Введіть текст у форматі "snake_case": ')
x = "".join(text.title().split("_"))
print('Конвертований текст у формат CapitalizedWords:', x)