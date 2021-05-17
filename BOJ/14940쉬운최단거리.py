import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i,j):
    visited[i][j] = 0
    deq.append([i,j,1])
    while deq:
        a,b,cnt= deq.popleft()
        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if 0<=x<n and 0<=y<m and visited[x][y] == -1:
                if board[x][y] == 1:
                    deq.append([x,y,cnt+1])
                    visited[x][y] += cnt+1
    return  
 
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
deq = deque()
visited = [[-1]*m for _ in range(n)]
check = True
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            bfs(i,j)
        elif board[i][j] == 0 :
            visited[i][j] = 0

for v in visited:
    print(' '.join(map(str,v)))
