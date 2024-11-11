n, k = map(int, input().split())

graph = [[1]*i for i in range(1, n+1)]

for i in range(2, n):
    for j in range(1, i):
        graph[i][j] = graph[i-1][j-1]+ graph[i-1][j]
print(graph[n-1][k-1])