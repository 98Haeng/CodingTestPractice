n = int(input())
scores = [int(input()) for _ in range(n)]

dp = scores[:]

for i in range(1, n):
    for j in range(i):
        # 이전거까지 누적해서 더해줘야 함.
        if scores[i] > scores[j]:
            # print(i, j)
            dp[i] = max(dp[i], dp[j] + scores[i])

print(max(dp))