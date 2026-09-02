arr = list(map(int, input().split()))
answer =[]
for val in arr:
    if val == 0:
        break
    elif val % 2 == 1:
        answer.append(val+3)
    else:
        answer.append(val// 2)

print(*answer)