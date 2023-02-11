def my_sum(*elements, start = 0):
    sum = 0
    for n in elements:
        sum += n + start
    print("Sum: ", sum)
my_sum(1, 2)
my_sum(1, 2, 3, 4)
my_sum(2, 4, 6, 8, 9)