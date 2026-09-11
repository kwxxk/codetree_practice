n = int(input())

matrix = [
    [0] * n
    for _ in range(n)
]

num = 1
for x in range(n):
    for y in range(n):
        matrix [y][x] = num
        num += 1
for row in matrix:
    print(*row)