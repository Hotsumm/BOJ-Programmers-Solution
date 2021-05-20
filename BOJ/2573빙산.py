import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    temp = deque()
    year = 0
    while ice:
        visited = [[0]*m for _ in range(n)]
        cnt = 1
        a,b = ice[0]
        temp.append([a,b])
        visited[a][b] = 1
        while temp:
            nx,ny = temp.popleft()
            for k in range(4):
                x = dx[k] + nx
                y = dy[k] + ny
                if 0<=x<n and 0<=y<m :
                    if not visited[x][y] and board[x][y] != 0:
                        cnt += 1
                        visited[x][y] = 1
                        temp.append([x,y])
        if len(ice) != cnt :
            return year
        
        visited = [[0]*m for _ in range(n)]
        for _ in range(len(ice)):
            nx,ny = ice.popleft()
            visited[nx][ny] = 1
            melted = 0
            for k in range(4):
                x = dx[k] + nx
                y = dy[k] + ny
                if 0<=x<n and 0<=y<m and not visited[x][y]:
                    if board[x][y] == 0:
                        melted += 1
    
            board[nx][ny] -= melted
            if board[nx][ny] <= 0:
                board[nx][ny] = 0
            else:
                ice.append([nx,ny])

        year += 1
            
     
    return 0


n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
ice = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] != 0:
            ice.append([i,j])

print(bfs())

