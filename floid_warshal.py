INF = int(1e9)

# 노드 개수 및 간선 개수 입력
n = int(input())
m = int(input())
# 2차원 리스트 만들고 모든 값 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신 -> 자기자신은 0으로
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아 그 값으로 초기화
for a in range(1, n+1):
    a, b, c = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우 무한으로
        if graph[a][b] == INF:
            print('INFINITY', end=' ')
        # 도달 가능한 경우 거리 출력
        else:
            print(graph[a][b], end=' ')
    print()