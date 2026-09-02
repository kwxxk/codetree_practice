n = int(input())

arr = []
arr.append(1)
arr.append(n)
i=2
while True:
    value = arr[i-2] + arr[i-1]
    arr.append(value)
    if value > 100:
        break
    i+=1

print(*arr)