arr = [
    list(map(int,input().split()))
    for _ in range(2)
]

for row in range(2):
    average = sum(arr[row])/len(arr[row])
    print(f"{average:.1f}", end = ' ')
print()
for col in range(4):
    col_sum = 0
    for row in range(2):
        col_sum += arr[row][col]

    average = col_sum /2
    print(f"{average:.1f}", end = ' ')

print()
total_sum =0
for row in range(2):
    total_sum += sum(arr[row])
total_average = total_sum / 8
print(f"{total_average:.1f}")