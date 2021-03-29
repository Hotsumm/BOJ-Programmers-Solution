import sys
sys.setrecursionlimit(10000)

n,m = map(int,sys.stdin.readline().split())
cnt = 0
def dfs(i):
    visited[i] = 1
    for j in range(1,n+1):
        if visited[j] == 0 and graph[i][j] == 1:
            dfs(j)

graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)

for i in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u][v] = 1
    graph[v][u] = 1

for i in range(1,n+1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1
print(cnt)

