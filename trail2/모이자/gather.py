n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
min_sum = float('inf')
for meeting_house in range(n):
    total_dis = 0
    for house in range(n):
        dis = abs(meeting_house-house)
        total_dis += dis * A[house]
    min_sum = min(min_sum,total_dis)
print(min_sum)