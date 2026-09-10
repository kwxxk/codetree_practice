n=int(input())
arr= list(map(int,input().split()))
list = []
for i in range(n):
    for j in range(1,n-i):
        list.append(arr[i+j]-arr[i])

print(min(list))