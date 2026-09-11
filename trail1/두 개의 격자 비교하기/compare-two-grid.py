n, m = map(int,input().split())
arr1 = [
    list(map(int,input().split()))
    for _ in range(n)
]
arr2 = [
    list(map(int,input().split()))
    for _ in range(n)
]
result = [
    [0] * m
    for _ in range(n)
]
for y in range(n):
    for x in range(m):
        if arr1[y][x] == arr2[y][x]:
            result[y][x] = 0
        else: result[y][x] = 1
for row in result:
    print(*row)