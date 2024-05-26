INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 것은 0으로
for a in range(1, n+1):
    for b in range(1, n+1):
        graph[a][b] = 0

# 경로 입력
for _ in range(1, n+1):
    # 서로가 가는 비용 : 1
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐갈 노드 x와 최종 목적지 노드 k 입력
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행 결과 출력
distance = graph[1][k] + graph[k][x]

# 도달 불가능한 경우 -1 출력
if distance >= INF:
    print("-1")
else:
    print(distance)
    
