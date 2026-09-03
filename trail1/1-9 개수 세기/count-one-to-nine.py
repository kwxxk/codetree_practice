n= int(input())
arr = list(map(int,input().split()))


for i in range(1,10):
    cnt = 0
    for val in arr:
        if i == val:
            cnt +=1
    print(cnt)