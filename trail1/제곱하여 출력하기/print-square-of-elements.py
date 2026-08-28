n=int(input())
arr = list(map(int, input().split()))
new_arr =[]
for val in arr:
    new_arr.append(val **2)
print(*new_arr)