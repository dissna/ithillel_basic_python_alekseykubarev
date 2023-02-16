def sign(x):
    if x > 0:
        result = 1
    elif x < 0:
        result = -1
    elif x == 0:
        result = 0
    return result


x = int(input("Enter the number: "))
print("Sign(x) =", sign(x))