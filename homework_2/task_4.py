from decimal import Decimal
grn = float(input("Введіть кількість гривень: "))
dol = Decimal(grn)/Decimal(36.76)
print('Станом на 30 січня 2022 року це становить', "%.2f"%dol, 'Долари США :(')
