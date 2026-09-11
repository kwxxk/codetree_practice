matrix  = [
    [0] * 5
    for _ in range(5)
]
for y in range(5):
    for x in range(5):
        matrix[y][0] = 1
        matrix[0][x] = 1
        matrix[y][x] = matrix[y-1][x] + matrix[y][x-1]
for row in matrix:
    print(*row)
