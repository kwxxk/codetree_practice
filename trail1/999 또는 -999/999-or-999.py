arr = list(map(int,input().split()))
if arr[-1] == -999 or arr[-1] == 999:
    arr.pop()
print(max(arr), min(arr))