n, m = map(int, input().split())

graph = []
visited = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

visited = [[False] * (n+1) for _ in range(m+1)]

# 갈 수 있는 방향
movex = [0, 1]
movey = [1, 0]

def dfs(x, y):
    # 방문했다고 인식
    global visited
    visited[y][x] = True

    # Yes 출력 조건
    if visited[m-1][n-1]:
        return 'Yes'


    # 이동할 수 있는 경우
    for i in range(len(movex)):
        nx = x + movex[i]
        ny = y + movey[i]
        # print(x, y)
        if 0 <= nx < n and 0 <= ny < m and visited[ny][nx] == False and graph[ny][nx] == 1:
            if dfs(nx, ny) == 'Yes':
                return 'Yes'
    return 'No'
print(dfs(0,0))