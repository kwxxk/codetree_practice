arr = [
    list(map(int,input().split()))
    for _ in range(4)
]
total_sum = 0
for row in range(4):
    for col in range(4):
        if col > row: continue
        total_sum += arr[row][col]
print(total_sum)