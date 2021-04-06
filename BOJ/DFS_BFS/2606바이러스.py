import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

def dfs(v):
    visited[v] = 1
    for i in range(n+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)
            
visited = [0] * (n+1)
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1
cnt = -1
dfs(1)
for i in range(1,n+1):
    if visited[i] == 1:
        cnt += 1
print(cnt)
