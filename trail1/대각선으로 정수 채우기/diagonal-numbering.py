n, m = map(int, input().split())

# Please write your code here.
matrix = [
    [0] * m
    for _ in range(n)
]
num = 1
for start_x in range(m):
    y = 0
    x = start_x

    while 0 <= y < n and 0 <= x < m:
        matrix[y][x] = num
        num +=1
        y += 1
        x -= 1

# 오른쪽 열에서 시작하는 대각선
for start_y in range(1, n):
    y = start_y
    x = m - 1

    while 0 <= y < n and 0 <= x < m:
        matrix[y][x] = num
        num +=1
        y += 1
        x -= 1

for row in matrix:
    print(*row)