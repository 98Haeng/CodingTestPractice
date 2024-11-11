from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# print(graph)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    que = deque()
    que.append((x,y))   
    while que:
        x, y = que.popleft()
        # 상하좌우 방향에서 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 무시하는 경우
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            # 가지 못하는 영역의 경우 안감
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx,ny))
                # print(nx, ny)
    return graph[n-1][m-1]

print(bfs(0,0))