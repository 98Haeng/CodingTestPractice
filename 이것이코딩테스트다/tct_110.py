## 알고리즘 : 구현 (시뮬레이션))

# 정사각형 크기
n = int(input())
# 이동
## L : 왼쪽
## U : 위쪽
## R : 오른쪽
## D : 아래쪽
#### R 이동시 (1, 1) -> (1, 2)
moves = list(map(str, input().split()))
x, y = 1, 1
# L, R, U D에 따른 이동
movex = [0, 0, -1, 1]
movey = [-1, 1, 0, 0]
press = ['L','R','U','D']

for move in moves:
    for i in range(len(press)):
        if move == press[i]:
            nx = x + movex[i]
            ny = y + movey[i]
    # 이동하지 못하는 조건
    if nx < 1 or ny < 1 or nx > n or ny > n:
        pass
    else:
        x, y = nx, ny
print(x, y)