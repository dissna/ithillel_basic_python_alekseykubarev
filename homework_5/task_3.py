def cone_square_and_volume(radius, height):
    pi = 22/7
    square = pi * radius * height + pi * radius ** 2
    volume = (pi * radius ** 2 * height) / 3
    return square, volume


radius = int(input("The radius of the cone: "))
height = int(input("The height of the cone: "))
print("Square: ", "%.2f" % cone_square_and_volume(radius, height)[0], "\n""Volume: ", "%.2f" % cone_square_and_volume(radius, height)[1])
