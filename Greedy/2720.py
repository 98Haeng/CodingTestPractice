quarter = 25
dime = 10
nickel = 5
penny = 1
changes = [25, 10, 5, 1]
# 테스트 케이스 개수
t = int(input())
# 입력
for _ in range(t):
    money = int(input())
    counts = []
    for i in changes:
        a = money // i
        counts.append(a)
        money -= i * a
    
    for i in counts:
        print(i, end=' ')