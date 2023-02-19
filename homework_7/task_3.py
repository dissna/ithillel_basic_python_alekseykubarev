print("Grains of rice on a chessboard (doubling every square):\n")

weight = 0
grains = 1
for square in range(1, 64+1):
    weight = grains * 0.000035 # 35 mg = 0.000035 kg
    print("sq{}|  grains = {}  weight = {}kg".format(square, grains, weight))
    grains *= 2