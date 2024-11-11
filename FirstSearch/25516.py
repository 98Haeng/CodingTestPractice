# 정점 수 n, 정수 k
# 정점 n개, n-1개의 간선
# 루트 노드에서 거리가 k 이하인 노드에 있는 사과를 수확하려 함
## output : 수확할 수 있는 사과 개수
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False] * (n+1)
# 간선 연결
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)

count = 0
# 사과가 있는 리스트
apples = list(map(int, input().split()))
def dfs(node, depth):
    global count
    visited[node] = True
    if depth <= k:
        count += apples[node]
    
    for i in graph[node]:
        if not visited[i]:
            dfs(i, depth + 1)
    return 
dfs(0,0)
print(count)

