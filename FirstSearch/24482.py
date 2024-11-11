import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
def dfs(v, count):
    visited[v] = count
    for i in sorted(graph[v], reverse=True):
        if visited[i] == -1:
            dfs(i, count+1)

    return

dfs(r,0)
print(*visited[1:], sep='\n')