import sys
input = sys.stdin.readline

n = int(input())
# 숫자들
nums = list(map(int, input().split()))

min_value = nums[0]
diffs = [0] * n
for i in range(len(nums)):
    # 이전까지 최소값 찾기
    min_value = min(min_value, nums[i])
    # 새로 게산하는 값, 기존 값 중에서 비교
    diffs[i] = max(diffs[i-1], nums[i]-min_value)

print(*diffs)