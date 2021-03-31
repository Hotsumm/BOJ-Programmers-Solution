
dx = [1,-1,0,0]
dy = [0,0,1,-1]            
def bfs(i,j):
    queue = [[i,j]]
    visited[0][0] = 1
    while queue:
        a,b = queue[0][0],queue[0][1]
        if a==n-1 and b==m-1:
            print(visited[a][b])
            break
        del queue[0]
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0<=x<n and 0<=y<m and maze[x][y] == 1 and visited[x][y] == 0:
                visited[x][y] = 1 + visited[a][b]
                queue.append([x,y])

n, m = map(int,input().split())

visited = [[0]*m for i in range(n)]
maze = []  
for _ in range(n):
    maze.append(list(map(int,input())))
bfs(0,0)
        
