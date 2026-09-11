n,m = map(int,input().split())
arr = [
    [0] * m
    for _ in range(n)
]

num = 1
for y in range(n):
    for x in range(m):
        arr[y][x] = num
        num +=1
for row in arr:
    for ele in row:
        print(ele, end= ' ')
    print()