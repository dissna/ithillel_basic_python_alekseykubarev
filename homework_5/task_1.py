import math
def degrees2radians(degree):
    radian = degree / (180/math.pi)
    return radian

degree = 60
print(degree, "\n""Radians: ", "%.4f" % math.cos(degrees2radians(degree)))
degree = 45
print(degree, "\n""Radians: ", "%.4f" % math.cos(degrees2radians(degree)))
degree = 40
print(degree, "\n""Radians: ", "%.4f" % math.cos(degrees2radians(degree)))