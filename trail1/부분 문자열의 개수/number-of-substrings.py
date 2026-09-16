input_str = input()
target_str = input()
cnt = 0
for j in range(len(input_str)):
    if input_str[j:j+len(target_str)] == target_str:
        cnt +=1
if cnt == 0: print(-1)
else: print(cnt)