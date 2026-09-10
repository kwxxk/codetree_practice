n,m = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
for val in arr:
    if m == val:
        cnt += 1
print(cnt)