n,m = map(int, input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(m)
]

matrix = [
    [0] * n
    for _ in range(n)
]
for y,x in arr:
    matrix[y-1][x-1] = y*x

for row in matrix:
    print(*row)