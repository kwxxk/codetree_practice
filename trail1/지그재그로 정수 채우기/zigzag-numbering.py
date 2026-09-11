n, m = map(int, input().split())

# Please write your code here.
matrix = [
    [0] * m
    for _ in range(n)
]
num =0
for x in range(m):
    if x % 2 == 0:
        for y in range(n):
            matrix[y][x] = num
            num += 1
    else:
        for y in range(n-1,-1,-1):
            matrix[y][x]= num
            num+=1
for row in matrix:
    print(*row)