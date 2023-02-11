import math
def degrees2radians(degree):
    radian = degree / (180/math.pi)
    return radian
degree = math.cos(60)
print(degree, "\n""Radians: ", "%.4f" % degrees2radians(degree))
degree = math.cos(45)
print(degree, "\n""Radians: ", "%.4f" % degrees2radians(degree))
degree = math.cos(40)
print(degree, "\n""Radians: ", "%.4f" % degrees2radians(degree))