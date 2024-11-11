n = int(input())

prices = list(map(int, input().split()))

benefit = 0
result = 0
for i in range(n-1, -1, - 1):
    benefit = max(prices[i], benefit)
    result = max(result, benefit - prices[i])

print(result)