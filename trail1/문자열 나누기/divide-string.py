n = int(input())
arr = input().split()

word = ''.join(arr)                    

a = (len(word) + 4) // 5

for j in range(a):
    print(word[5 * j:5 * (j + 1)])      