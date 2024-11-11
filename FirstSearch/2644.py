import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 재귀 제한을 늘립니다.

# 전체 사람 수
n = int(input())
# 찾아야 하는 두 사람 (촌수를 계산해야 하는 서로 다른 두사람)
a, b = map(int, input().split())
# 관계 개수
m = int(input())

graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)

for _ in range(m): 
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = -1  # 결과를 저장할 변수

def dfs(v, num):
    global result
    num += 1
    visit[v] = True

    if v == b:
        result = num - 1  # 최종 촌수는 num에서 1을 뺀 값
        return
    for i in graph[v]:
        if not visit[i]:
            dfs(i, num)

dfs(a, 0)

print(result)