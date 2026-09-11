arr = [
    input()
    for _ in range(3)
]
len_list = []
for string in arr:
    len_list.append(len(string))

print(max(len_list)-min(len_list))
