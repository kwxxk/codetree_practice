word = input()
word = word[:1] + 'a' + word[2:len(word)-2] + 'a' + word[-1]
print(word)