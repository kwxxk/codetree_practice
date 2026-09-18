r, c = map(int, input().split())
grid = [list(input().split()) for _ in range(r)]

# Please write your code here.
answer = 0
K = 2


def dfs(y, x, jumps):
    global answer

    if y == r - 1 and x == c - 1:
        if jumps == K+1: answer+=1
        return

    for ny in range(y + 1, r):
        for nx in range(x + 1, c):
            if grid[ny][nx] != grid[y][x]:
                dfs(ny, nx, jumps + 1)


dfs(0, 0, 0)
print(answer)