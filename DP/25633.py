# 해결 못함
import sys
input = sys.stdin.readline

n = int(input().strip())
domino = list(map(int, input().strip().split()))

# dp = [1] * n

# for i in range(1, n):
#     for j in range(i-1, -1, -1):
#         if j + domino[j] >= i:  # 이전 도미노가 현재 도미노까지 도달할 수 있는지 확인
#             dp[i] = max(dp[i], dp[j] + 1)

# print(max(dp))
def max_domino_sequence(N, weights):
    dp = [1] * N  # Initialize the dp array with 1 as each domino can stand alone
    
    for i in range(1, N):
        cumulative_sum = weights[i - 1]
        for j in range(i - 1, -1, -1):
            if cumulative_sum >= weights[i]:
                dp[i] = max(dp[i], dp[j] + 1)
            cumulative_sum += weights[j - 1] if j > 0 else 0
    
    return max(dp)
print(max_domino_sequence(n, domino))