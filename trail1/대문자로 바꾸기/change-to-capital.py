arr = [
    list(input().split())
    for i in range(5)
]
for row in arr:
    row = [char.upper() for char in row]
    print(*row)