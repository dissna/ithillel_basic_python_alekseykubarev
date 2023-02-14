import math
import cmath

def solve_quadratic_equation(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + math.sqrt(d))/2*a
        x2 = (-b - math.sqrt(d))/2*a
        result = "Discriminator: %s \n x1 = %s \n x2 = %s \n" % (d, x1, x2)
    elif d == 0:
        x1 = -b/2*a
        result = "Discriminator: %s \n x1 = %s \n" % (d, x1)
    else:
        x1 = (-b + cmath.sqrt(d)) / 2 * a
        x2 = (-b - cmath.sqrt(d)) / 2 * a
        result = "Complex roots\nDiscriminator: %s \n x1 = %s \n x2 = %s \n" % (d, x1, x2)
    return result


print("ax^2 + bx + c = 0")
a = int(input("Enter value 'а': "))
b = int(input("Enter value 'b': "))
c = int(input("Enter value 'c': "))
print(solve_quadratic_equation(a, b, c))