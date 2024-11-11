# 연산 조건 
## 1. n-1
## 2. n/k (나누어 떨어질때만)
### -> n을 1로 만드는 연산 최소 횟수

n, m = map(int, input().split())
count = 0
# n이 m보다 크거나 같을 때
while n>=m:
    if n%m==0:
        count+=1
        n = n//m
    else:
        n = n-1
        count += 1

while n > 1:
    n -= 1
    count += 1
print(count)