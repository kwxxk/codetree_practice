n = int(input())
arr = [
    input()
    for _ in range(n)
]
word = ''
for i in range(n):
    word += arr[i]

print(word)