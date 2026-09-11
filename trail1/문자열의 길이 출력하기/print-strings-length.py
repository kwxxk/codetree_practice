arr = [
    input()
    for _ in range(2)
]
total_len = 0
for char in arr:
    total_len += len(char)
print(total_len)