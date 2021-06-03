import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i):
    deq = deque()
    deq.append([0,i])
    while deq:
        a,b = deq.popleft()
        if a == m-1:
            return True
        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if 0<=x<m and 0<=y<n:
                if not visited[x][y] and fiber[x][y] == 0:
                    deq.append([x,y])
                    visited[x][y] = 1
    return False

m,n = map(int,input().split())
fiber =  [list(map(int,input().strip())) for _ in range(m)]
visited = [[0]*n for _ in range(m)]
answer = 0
for i in range(n):
    if fiber[0][i] == 0:
        if bfs(i):
            answer = 1
if answer:
    print('YES')
else:
    print('NO')