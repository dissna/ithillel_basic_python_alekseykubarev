def fibonacci(x):
    if x in (2, 3):
        result = 1
    elif x == 1:
        result = 0
    else:
        result = fibonacci(x - 1) + fibonacci(x - 2)
    return result


x = int(input("Fibonacci sequences start with numbers 0 and 1 \nEnter the element number of the Fibonacci series: "))
print("Result: ", fibonacci(x))