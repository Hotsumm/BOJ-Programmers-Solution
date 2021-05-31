import sys
from collections import deque
input = sys.stdin.readline


dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i,j,g):
    visited[i][j] = 1
    arr[i][j] = g
    deq.append((i,j))
    cnt = 1
    while deq:
        nx,ny = deq.popleft()
        for k in range(4):
            x = dx[k] + nx
            y = dy[k] + ny
            if 0<=x<n and 0<=y<m :
                if not visited[x][y] and arr[x][y] == 1:
                    visited[x][y] = 1
                    deq.append((x,y))
                    arr[x][y] = g
                    cnt += 1 
    dt[g] = cnt
    

n,m = map(int,input().split())
answer = []
temp = []
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
g = 2
dt = dict()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            deq = deque()
            bfs(i,j,g)
            g += 1
        elif arr[i][j] == 0:
            temp.append([i,j])

for i,j in temp:
    result = 1
    visited = []
    for k in range(4):
        x = dx[k] + i
        y = dy[k] + j
        if 0<=x<n and 0<=y<m:
            if arr[x][y] != 0 and arr[x][y] not in visited:
                result += dt[arr[x][y]]
                visited.append(arr[x][y])
    answer.append(result)

print(max(answer))
