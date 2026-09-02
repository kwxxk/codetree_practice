n = int(input())

arr = [n * i for i in range(1,11)]
cnt = 0
answer = []
for val in arr:
    if val % 5 == 0:
        cnt +=1
        
        if cnt == 2:
            answer.append(val)
            break
    answer.append(val)

print(*answer)