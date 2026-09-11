arr1 = [
    list(map(int, input().split()))
    for _ in range(3)
]
input()
arr2 = [
    list(map(int, input().split()))
    for _ in range(3)
]
result = [
    [0] * 3
    for _ in range(3)
]

for y in range(3):
    for x in range(3):
        result[y][x] = arr1[y][x] * arr2[y][x]

for row in result:
    print(*row)