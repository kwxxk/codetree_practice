arr = ['L','E','B','R','O','S']

char = input()
idx = -1
for i in range(len(arr)):
    if char == arr[i]:
        idx = i
        
if idx == -1:
    print(None)
else:
    print(idx)