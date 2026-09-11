n = int(input())
matrix = [
    [0] * n
    for _ in range(n)
]
num = 1
for x in range(n-1,-1,-1):
    order = n - 1 -x
    if order % 2 == 0:
        for y in range(n-1,-1,-1):
            matrix[y][x] = num
            num +=1
    else:
        for y in range(n):
            matrix[y][x] = num
            num +=1
for row in matrix:
    print(*row)