import math

def circles_intersect(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return intersect if d <= r1 + r2 else not_intersect


intersect = 'intersect'
not_intersect = 'not intersect'
x1 = float(input('Enter the x-coordinate of the first circle: '))
y1 = float(input('Enter the y-coordinate of the first circle: '))
r1 = float(input('Enter the radius of the first circle: '))
x2 = float(input('Enter the x-coordinate of the second circle: '))
y2 = float(input('Enter the y-coordinate of the second circle: '))
r2 = float(input('Enter the radius of the second circle: '))
print("Circles C1 and C2 {}".format(circles_intersect(x1, y1, r1, x2, y2, r2)))