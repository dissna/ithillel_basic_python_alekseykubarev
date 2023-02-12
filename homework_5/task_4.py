def my_sum(*elements, start = 0):
    return sum(elements) + start

print("Sum: ", my_sum(1, 2))
print("Sum: ", my_sum(1, 2, 3, 4))
print("Sum: ", my_sum(2, 4, 6, 8, 9))