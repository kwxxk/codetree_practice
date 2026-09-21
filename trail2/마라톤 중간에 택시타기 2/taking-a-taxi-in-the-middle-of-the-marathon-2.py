n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

min_dis = float('inf')
for j in range(1,len(x)-1):
    dis = 0
    x1 = x.copy()
    y1 = y.copy()
    x1.pop(j)
    y1.pop(j)

    for i in range(len(x1) - 1):
        dis += abs(x1[i] - x1[i+1]) + abs(y1[i]-y1[i+1])
    min_dis = min(min_dis,dis)
print(min_dis)