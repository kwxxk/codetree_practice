n = int(input())
a = list(map(int, input().split()))
mincnt =0
for i in range(n):
    if a[i] == min(a):
        mincnt +=1
    
print(min(a),mincnt)