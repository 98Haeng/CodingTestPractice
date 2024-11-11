n = int(input())
times = list(map(int, input().split()))
# 작은 순서대로 정렬해야 함
times.sort()
total_time = 0
# 작은 것을 많이 더할수록 최소값이 나옴
for i in range(len(times)):
    total_time += times[i] * (len(times)-i)
print(total_time)