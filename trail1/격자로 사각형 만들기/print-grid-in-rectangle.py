n= int(input())
matrix = [
    [0] * n
    for _ in range(n)
]
for y in range(n):
    for x in range(n):
        matrix[y][0] = 1
        matrix[0][x] = 1
        matrix[y][x] = matrix[y-1][x-1] + matrix[y-1][x] + matrix[y][x-1]

for row in matrix:
    print(*row)