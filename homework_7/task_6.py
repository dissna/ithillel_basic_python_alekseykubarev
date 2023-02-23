def fibonacci(x):
    a = 0
    b = 1
    if x == 0:
        return 0
    elif x == 1:
        return b
    for i in range(2, x):
        c = a + b
        a = b
        b = c
    return b


x = int(input("Fibonacci sequences start with numbers 0 and 1 \nEnter the element number of the Fibonacci series: "))
print("Result:", fibonacci(x))