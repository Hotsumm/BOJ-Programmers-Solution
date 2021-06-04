# pypy3
from collections import deque
import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i,j):
    cnt = -1
    visited[i][j] = 1
    deq.append([i,j])
    while deq:
        for _ in range(len(deq)):
            a,b = deq.popleft()
            for k in range(4):
                x = dx[k] + a
                y = dy[k] + b
                if 0<=x<n and 0<=y<m:
                    if not visited[x][y] and p[x][y] == 'L':
                        visited[x][y] = 1
                        deq.append([x,y])
        cnt += 1
    return cnt
                    

n,m = map(int,input().split())

p = [list(input().strip()) for _ in range(n)]
deq = deque()
answer = 0
for i in range(n):
    for j in range(m):
        if p[i][j] == 'L':
            visited = [[0]*m for _ in range(n)]
            answer = max(answer,bfs(i,j))

print(answer)

