n = int(input())
matrix = [
    [0] * n
    for _ in range(n)
]
for y in range(n):
    matrix[y][0] = 1
    matrix[y][y] = 1
    for x in range(1,y):
        matrix[y][x] = matrix[y-1][x-1] + matrix[y-1][x]

for row in matrix:
    print(*(val for val in row if val !=0))