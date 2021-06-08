from collections import deque
import sys
input = sys.stdin.readline


dx = [1,-1,0,0]
dy = [0,0,1,-1]

def melting(i,j):
    check = False
    visited[i][j] = 1
    deq = deque()
    deq.append([i,j])
    while deq:
        nx,ny = deq.popleft()
        for k in range(4):
            x = dx[k] + nx
            y = dy[k] + ny
            if 0<=x<n and 0<=y<m and not visited[x][y]:
                if cheese[x][y] == 0:
                    deq.append([x,y])
                    visited[x][y] = 1
                else :
                    check = True
                    cheese[x][y] += 1
    return check
                    

n,m = map(int,input().split())
cheese = [list(map(int,input().split())) for _ in range(n)]
answer = 0
while True:
    visited = [[0]*m for _ in range(n)]
    if melting(0,0):
        for i in range(n):
            for j in range(m):
                if cheese[i][j] >=3 :
                    cheese[i][j] = 0
                elif cheese[i][j] == 2:
                    cheese[i][j] = 1
        answer += 1
    else:
        break
print(answer)

