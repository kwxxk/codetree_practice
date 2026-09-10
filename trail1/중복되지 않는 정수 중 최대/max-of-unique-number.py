n = int(input())
nums = list(map(int, input().split()))
answer = []
# Please write your code here.
for number in nums:
    if nums.count(number) == 1:
        answer.append(number)

if len(answer) == 0:
    print(-1)
else:
    print(max(answer))
