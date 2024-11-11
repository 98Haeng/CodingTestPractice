n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
result = 0
# 이진 탐색
while (start <= end):
    total = 0
    mid = (start + end) // 2
    # 자르고 남는 총합 계산 (손님이 가져가는 양)
    for i in arr:
        if i > mid:
            total += i - mid
    # 총합이 m보다 작을 때
    if total < m:
        end  = mid - 1
    # 총합이 m보다 클 때
    else:
        result = mid
        start = mid + 1
print(result)