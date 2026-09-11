char = input()
target = input()

cnt = 0
for ch in char:
    if target == ch:
        cnt +=1
print(cnt)
