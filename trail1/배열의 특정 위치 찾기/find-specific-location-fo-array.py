arr = list(map(int, input().split()))
even_sum = 0
three_sum = 0
three_cnt = 0
for i in range(10):
    if (i+1) % 2 == 0:
        even_sum += arr[i]
    if (i+1) % 3 == 0:
        three_sum += arr[i]
        three_cnt += 1
average = three_sum/ three_cnt

print(f"{even_sum} {average:.1f}")