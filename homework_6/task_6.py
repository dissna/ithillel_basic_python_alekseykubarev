def sign(x):
    if x > 0:
        result = "Sign(x) = 1"
    elif x < 0:
        result = "Sign(x) = -1"
    elif x == 0:
        result = "Sign(x) = 0"
    return result


x = int(input("Enter the number: "))
print(sign(x))