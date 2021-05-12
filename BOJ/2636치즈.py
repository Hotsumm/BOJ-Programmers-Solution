import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i,j):
    visited[i][j] = 1
    deq.append([i,j])
    cnt = 0
    while deq:
        nx,ny = deq.popleft()
        for k in range(4):
            x = dx[k] + nx
            y = dy[k] + ny
            if 0<=x<n and 0<=y<m and not visited[x][y]:
                if cheese[x][y] == 1:
                    cheese[x][y] = 2
                elif not cheese[x][y]:
                    deq.append([x,y])
                visited[x][y] = 1
    for a in range(n):
        for b in range(m):
            if cheese[a][b] == 1 or cheese[a][b] == 2:
                cnt += 1 
            if cheese[a][b]==2:
                cheese[a][b] = 0
    return cnt 

n,m = map(int,input().split())
cheese = [list(map(int,input().split())) for _ in range(n)]

answer = 0
last_cheese = 0
while True:
    deq = deque()
    visited = [[0]*m for _ in range(n)]
    check = bfs(0,0)
    if not check:
        break
    last_cheese = check
    answer += 1
print(answer)
print(last_cheese)