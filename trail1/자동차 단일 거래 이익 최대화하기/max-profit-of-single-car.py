n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
max_profit = 0
profit = []
for i in range(n):
    for j in range(n-i):
        profit.append(price[i+j] - price[i])
max_profit = max(profit)
print(max_profit)