n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(m)
]
matrix = [
        [0] * n
        for _ in range(n)
    ]
for val in arr:
    y,x = val[0],val[1]
    
    matrix[y-1][x-1] = 1
for row in matrix:
    print(*row)