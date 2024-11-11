# 공연장 크기 입력
c, r = map(int, input().split())
# 대기번호
k = int(input())
seats = [[False for _ in range(c + 1)] for _ in range(r + 1)]
def move(x,y):
    global seats
    # x,y : 공연장 크기
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    tmp = 1
    i = 0
    while True:
        # 시도 횟수만큼 이동했을 때 (종료시점)
        if tmp == k:
            return x+1, y+1
        seats[y][x] = True
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < c and 0 <= ny < r): # 사각형 범위 안에 있을 때
            if seats[ny][nx] == False: # 들르지 않았을 때
                x = nx
                y = ny
                tmp += 1
            else: # 지나간 점이면 방향 바꾸기
                i = (i+1) % 4
        else: # 다음 점이 벗어나면 방향 바꾸기
            i = (i+1) % 4
if k > c*r:
    print(0)
else:
    print(move(0,0))