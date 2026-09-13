n= int(input())
arr = [
    input()
    for _ in range(n)
]
cnt =0
sum = 0 
for word in arr:
    sum += len(word)
    if word[0] == 'a':
        cnt+=1
print(sum,cnt)