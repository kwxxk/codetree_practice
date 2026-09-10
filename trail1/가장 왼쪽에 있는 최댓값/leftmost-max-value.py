n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
end = len(a)
idxlist = []
while end > 0:
    max_val = max(a[:end])
    for i in range(end):
        if a[i] == max_val:
            end = i
            idxlist.append(i+1)
            break
print(*idxlist)
    