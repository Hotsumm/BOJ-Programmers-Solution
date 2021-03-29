import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y):
    queue = [[x,y]]
    while queue:
        a,b = queue[0][0],queue[0][1]
        del queue[0]
        for i in range(4):
            q = a + dx[i]
            w = b + dy[i]
            if 0<=q<n and 0<=w<m and graph[q][w]==1:
                graph[q][w] = 0
                queue.append([q,w])

t = int(sys.stdin.readline())
for _ in range(t):
    cnt = 0
    m,n,k = map(int,sys.stdin.readline().split())   
    graph = [[0] * m for i in range(n)]
    for i in range(k):
        x, y = map(int,sys.stdin.readline().split())
        graph[y][x] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i,j)
                cnt +=1 
    print(cnt)
