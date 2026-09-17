word = list(input().strip())
first = word[0]
second = word[1]
for i in range(len(word)):
    if word[i] == first:
        word[i] = second
    elif word[i] == second:
        word[i] = first
print(*word,sep='')