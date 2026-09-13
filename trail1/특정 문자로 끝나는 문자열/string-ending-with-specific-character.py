arr = [
    input()
    for _ in range(10)
]
char = input()
target_list = []
for word in arr:
    if char == word[-1]:
        target_list.append(word)

if not target_list: print("None")
else: 
    for target in target_list: print(target)
    
