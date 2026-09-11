char1, char2 = input().split()
if len(char1) == len(char2): print('same')
else:
    if len(char1) > len(char2):
        print(char1, len(char1))
    else:
        print(char2, len(char2))