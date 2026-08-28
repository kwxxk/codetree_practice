arr = list(map(int, input().split()))

odd_arr = []
even_arr =[]
for idx in range(len(arr)):
    if (idx + 1) % 2== 1:
        odd_arr.append(arr[idx])
    else:
        even_arr.append(arr[idx])

cal = abs(sum(odd_arr) - sum(even_arr))
print(cal)