##### 메모이제이션 방법으로 풀기
n = int(input())
array = list(map(int, input().split()))

# 기억 변수
d = [0] * 101

# Bottom Up 방식
d[0] = array[0]
d[1] = array[1]
for i in range(2, n+1):
    # 피보나치와 같은 원리
    d[i] = max(d[i-1], d[i-2] + array[i])
print(d[n-1])