def knight_moves(x0, y0):
    moves = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]
    validPositions = []
    x1 = x0 - 96
    for (x, y) in moves:
        xNew = x1 + x
        yNew = y0 + y
        if 1 < xNew < 8 and 1 < yNew < 8:
            validPositions.append([chr(xNew+96), yNew])
    return validPositions


x0 = ord('{}'.format(str(input("Enter the starting cell of the knight (a-h): "))))
y0 = int(input("Enter the starting cell of the knight (1-8): "))
print("All possible moves of the knight: ", knight_moves(x0, y0))