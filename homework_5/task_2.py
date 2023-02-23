def triangle_square_and_perimeter(a, b):
    s = 1/2 * (a * b)
    p = a + b + (a**2 + b**2)**0.5
    return s, p


a = int(input("Input the first side about the right angle of a triangle: "))
b = int(input("Input the second side about the right angle of a triangle: "))
print("Square: ", triangle_square_and_perimeter(a, b)[0], "\n""Perimeter: ", triangle_square_and_perimeter(a, b)[1])