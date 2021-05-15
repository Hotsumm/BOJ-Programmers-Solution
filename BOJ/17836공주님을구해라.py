import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i,j,t):
    deq = deque()
    visited[i][j] = 1
    deq.append((i,j,0))
    while deq:
        a,b,time= deq.popleft()
        if t<time:
            return
        elif a == n-1 and b == m-1:
            answer.append(time)
            return
        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if 0<=x<n and 0<=y<m and not visited[x][y]:
                if castle[x][y] == 0 :
                    deq.append((x,y,time+1))
                    visited[x][y] = 1
                elif castle[x][y] == 2:
                    if time+(n-1-x)+(m-1-y)+1 <= t:
                        answer.append(time+(n-1-x)+(m-1-y)+1)
                         
    return 
 
n,m,t = map(int,input().split())
answer = []
castle = []
for _ in range(n):
    castle.append(list(map(int,input().split())))
visited = [[0]*m for _ in range(n)]
bfs(0,0,t)
if answer:
    print(min(answer))
else:
    print("Fail")
