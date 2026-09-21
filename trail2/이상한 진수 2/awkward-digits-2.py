a = input()
arr = []
for i in range(len(a)):
# Please write your code here.
    arr += a[i]
for j in range(len(arr)): # arr 구성에서 전부 다 1로 구성이면 arr[-1]을 0으로 바꾸고 , 이외에는 첫번째 0을 1로 바꿈
    if arr[j] == '0':
        arr[j] = '1'
        break
else: arr[-1] = '0'
answer = 0
for k in range(len(arr)):
    answer += int(arr[k]) * (2**(len(arr)-1-k))
print(answer)
