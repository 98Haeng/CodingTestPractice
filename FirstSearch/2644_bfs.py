from collections import deque
# 전체 사람 수
n = int(input())
# 찾아야 하는 두 사람 (촌수를 계산해야 하는 서로 다른 두사람)
a, b = map(int, input().split())
# 관계 개수
m = int(input())

graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)
# print(visit)
result = []
# 그래프 추가
for _ in range(m): 
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 너비 우선 탐색 시행
def bfs(start):
    queue = deque([(start, 0)]) 
    visit[start] = True

    while queue:
        current, count = queue.popleft(0)

        if current == b:
            return count

        for n in graph[current]:
            if not visit[n]:
                visit[n] = True
                queue.append((n, count + 1))

    return -1

result = bfs(a)
print(result)