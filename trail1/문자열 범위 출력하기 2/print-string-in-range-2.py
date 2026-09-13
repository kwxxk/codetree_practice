char = input()
n= int(input())

if len(char) > n:
    print(char[len(char)-1:len(char)-n-1:-1])
else: print(char[::-1])