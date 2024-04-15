n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# dfs 함수
def dfs(x, y):
    # 주어진 범위 벗어나는 경우 즉시 종료
    if x<=-1 or y<=-1 or x>=n or y>=n:
        return False
    if graph[x][y]==0:
        # 방문처리
        graph[x][y] = 1
        # 상하좌우 재귀 호출
        dfs(x-1,y) # 좌
        dfs(x+1,y) # 우
        dfs(x,y-1) # 하
        dfs(x,y+1) # 상
        # 4개가 모두 맞으면 True 반환
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

# 채우기

print(result)
