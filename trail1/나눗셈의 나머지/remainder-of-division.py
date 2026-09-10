a,b = map(int,input().split())
arr = [0] * b
while a > 1:
    a,val = divmod(a,b)
    arr[val] += 1
sum_square = 0
for value in arr:
    sum_square += value ** 2
print(sum_square)
