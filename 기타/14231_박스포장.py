# 박스 개수
n = int(input())
boxes = list(map(int, input().split()))

dp = [1] * n

# 앞의 박스를 무조건 뒤에 넣어야 함.
for i in range(1, n):
    for j in range(i):
        if boxes[j] < boxes[i]:
            dp[i] = max(dp[i], dp[j] + 1)
max_boxes = max(dp)
# print(dp)
print(max_boxes)