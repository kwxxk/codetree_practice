word = input()
word_fp = ''
for i in range(len(word)):
    if i% 2 == 0: continue
    word_fp += word[i]

print(word_fp[::-1])
    