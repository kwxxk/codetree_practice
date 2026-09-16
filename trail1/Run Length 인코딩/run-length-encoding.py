text = input().strip()
result = []

current_char = text[0]
count = 1

for i in range(1, len(text)):
    if text[i] == current_char:
        count +=1
    else:
        result.append(current_char+str(count))
        current_char = text[i]# 현재 문자와 개수를 result에 추가
        # 현재 문자 변경

        count = 1 # 개수 초기화

result.append(current_char + str(count))
encoded = ''.join(result)
print(len(encoded))
print(''.join(result))