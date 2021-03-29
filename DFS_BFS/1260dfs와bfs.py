n,m,v = map(int,input().split())

def dfs(v):
    visited[v] = 1
    print(v,end=' ')
    for i in range(1,n+1):
        if visited[i]==0 and graph[v][i]==1:
            dfs(i)
            
def bfs(v):
    queue = [v]
    visited[v] = 0
    while queue:
        v = queue[0]    
        print(v,end=' ')
        del queue[0]
        for i in range(1, n+1):
            if visited[i]==1 and graph[v][i]==1:
                queue.append(i)
                visited[i] = 0
        
visited = [0 for _ in range(n+1)]
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1


dfs(v)
print()
bfs(v)
