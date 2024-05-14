n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

# 존재하는 경우 vs 존재하지 않는 경우
d = [10001] * (m+1)

# DP 진행
# 금액 0을 만드는데 필요한 화폐 0개
d[0] = 0
# 순환 동적 프로그래밍 수행
for i in range(n):
    for j in range(arr[i], m+1):
        # 현재 금액 j에서 화폐 단위 arr[i]를 뺀 금액을 만드는 것이 가능한지
        if d[j-arr[i]] != 10001:
            # 최소 화폐개수에 하나 추가
            d[j] = min(d[j], d[j-arr[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])