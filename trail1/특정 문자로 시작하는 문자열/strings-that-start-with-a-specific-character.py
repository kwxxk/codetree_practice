n = int(input())
arr = [
    input()
    for _ in range(n)
]
ch = input()
cnt = 0
sum = 0
length = 0
for word in arr:
    if word[0] == ch:
        cnt+=1
        sum += len(word)
length = sum/cnt
print(f"{cnt} {length:.2f}")