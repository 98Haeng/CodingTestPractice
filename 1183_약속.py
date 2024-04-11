n = int(input())
times = []
for _ in range(n):
    a, b = map(int, input().split())
    times.append(b-a)

# 먼저 도착한 사람이 늦게 도착한 사람까지 기다리기
# 정렬
times.sort()

# print(times)
if n%2==1:
    print(1)
else:
    # 중앙 2개의 값
    print(abs(times[n//2] - times[n//2-1])+1)
