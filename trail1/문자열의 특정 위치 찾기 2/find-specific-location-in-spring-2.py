char = input()
char_list = ["apple", "banana", "grape", "blueberry", "orange"]
cnt = 0
for word in char_list:
    if char == word[2] or char == word[3]:
        cnt+=1
        print(word)
print(cnt)