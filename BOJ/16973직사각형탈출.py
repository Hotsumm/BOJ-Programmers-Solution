import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(h,w,sr,sc,fr,fc):
    visited[sr][sc] = 1
    deq.append([sr,sc,0])
    while deq:
        a,b,cnt= deq.popleft()
        if a == fr and b == fc:
            return cnt
        for k in range(4):
            check = True
            x = dx[k] + a
            y = dy[k] + b
            if 0<=x<n and 0<=y<m and x<=h+x<n and y<=w+y<m and not visited[x][y]:
                if wall:
                    for i,j in wall:
                        if x<=i<=h+x and y<=j<=w+y:
                            check = False
                            break
                if check:
                    deq.append([x,y,cnt+1])
                    visited[x][y] = 1
    return -1 
 
n,m = map(int,input().split())
board = []
wall = []
for _ in range(n):
    board.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            wall.append([i,j])

visited = [[0]*m for _ in range(n)]
h,w,sr,sc,fr,fc = map(int,input().split())
deq = deque()
print(bfs(h-1,w-1,sr-1,sc-1,fr-1,fc-1))
