n = int(input())
arr = list(map(int,input().split()))
list = []
for i in range(len(arr)):
    if arr[i] == 2:
        list.append(i+1)
print(list[2])
