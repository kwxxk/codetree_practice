arr = list(map(int,input().split()))
for i in range(1,10):
    cnt = 0
    for val in arr:
        if val == 0:
            break
        if i == (val//10):
            cnt += 1
    print(f"{i} - {cnt}")
    