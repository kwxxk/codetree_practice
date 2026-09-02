n = int(input())
arr = list(map(int,input().split()))
answer = []
for val in arr:
    if val % 2 ==0:
        answer.append(val)

print(*answer)