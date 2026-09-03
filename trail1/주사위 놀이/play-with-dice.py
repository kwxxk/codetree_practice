arr = list(map(int, input().split()))
for i in range(1,7):
    cnt = 0
    for val in arr:
        if i == val:
            cnt +=1
    print(f"{i:} - {cnt}")