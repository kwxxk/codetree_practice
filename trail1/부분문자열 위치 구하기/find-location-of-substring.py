input_str = input()
target_str = input()

# Please write your code here.
answer = -1 
for j in range(len(input_str) - len(target_str) + 1):
    if input_str[j:j+len(target_str)] == target_str:
        answer = j
        break
print(answer)