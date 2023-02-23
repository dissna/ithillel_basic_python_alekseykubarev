def sum_symbol_codes(first, second):
    x = ord(first)
    y = ord(second)
    if x == y:
        return x
    if x < y:
        list_value = list(range(x, y + 1, 1))
        return sum(list_value)
    if x > y:
        list_value = list(range(x, y + 1, 1))
        return sum(list_value)


first = str(input("Input first element: "))
second = str(input("Input second element: "))
print('Result:', sum_symbol_codes(first, second))