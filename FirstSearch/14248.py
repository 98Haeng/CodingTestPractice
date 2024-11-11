import sys
input = sys.stdin.readline

n=  int(input())
lists = list(map(int, input().split()))
visited = [0] * (n+1)
s = int(input())

count = 1
def dfs(x):
    global count
    for i in range(2):
        if i==0:
            nx = x + lists[x]
        else:
            nx = x - lists[x]

        if 0 <= nx < n and visited[nx] == 0:
            visited[nx] = 1
            count += 1
            dfs(nx)

dfs(s-1)
print(count)
