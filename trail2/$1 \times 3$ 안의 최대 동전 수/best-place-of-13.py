n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
max_coin = 0
# Please write your code here.
for y in range(n):
    for x in range(n-2):
        coin = sum(grid[y][x:x+3])
        max_coin = max(max_coin,coin)
print(max_coin)
