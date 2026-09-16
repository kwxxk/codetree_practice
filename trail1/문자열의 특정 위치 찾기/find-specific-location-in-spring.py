word,target = input().split()
target_list = []
for i in range(len(word)):
    if word[i] == target:
        target_list.append(i)

if not target_list:
    print('No')
else:
    print(target_list[0])