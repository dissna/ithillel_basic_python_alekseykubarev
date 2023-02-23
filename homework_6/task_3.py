import math
import cmath

def solve_quadratic_equation(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b+math.sqrt(d))/2*a
        x2 = (-b-math.sqrt(d))/2*a
        return x1, x2
    elif d == 0:
        x1 = -b/2*a
        x2 = None
        return x1, x2
    else:
        sol1 = (-b-cmath.sqrt(d))/2*a
        sol2 = (-b+cmath.sqrt(d))/2*a
        return sol1, sol2


print("ax^2 + bx + c = 0")
a = int(input("Enter value 'а': "))
b = int(input("Enter value 'b': "))
c = int(input("Enter value 'c': "))
print("Solution to the entered quadratic equation: ", solve_quadratic_equation(a, b, c))