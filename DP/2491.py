n = int(input())

nums = list(map(int, input().split()))
max_length = 0 # 가장 긴 길이
count = 1

# 연속되는 값 표시
g1 = [1] * n
g2 = [1] * n

# 증가할 때 
for i in range(1, len(nums)):
    # 이전보다 클 때
    if nums[i] >= nums[i-1]:
        g1[i] += g1[i-1]
# 감소할 때
for i in range(1, len(nums)):
    if nums[i] <= nums[i-1]:
        g2[i] += g2[i-1]

print(max(max(g1), max(g2)))