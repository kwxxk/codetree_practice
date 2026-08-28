arr= list(map(int, input().split()))
sarr =[]
for i in arr:
    if i ==0:
        break
    else:
        sarr.append(i)

total = sum(sarr[-3::])
print(total)
