def cone_square_and_volume(radius, height):
    Square = 22 / 7 * radius * height + 22 / 7 * radius ** 2
    Volume = (22 / 7 * radius ** 2 * height) / 3
    return Square, Volume
radius = int(input("The radius of the cone: "))
height = int(input("The height of the cone: "))
print("Square: ", "%.2f" % cone_square_and_volume(radius, height)[0], "\n""Volume: ", "%.2f" % cone_square_and_volume(radius, height)[1])
