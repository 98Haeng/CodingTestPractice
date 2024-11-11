# 참가자 수, 지민, 한수 순서
n, a, b = map(int, input().split())
cnt=0
while a!=b:
    a -= a//2
    b -= b//2
    cnt+=1

print(cnt)