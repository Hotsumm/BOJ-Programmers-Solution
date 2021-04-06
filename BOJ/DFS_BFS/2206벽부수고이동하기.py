# 3차원 배열안하면 시간초과 

import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs():
    queue.append([0,0,0])
    visited[0][0][0] = 1
    while queue:
        a,b,z = queue.popleft()
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0<=x<n and 0<=y<m :
                if graph[x][y] == 0 and visited[x][y][z] == -1:
                    visited[x][y][z] = visited[a][b][z] + 1
                    queue.append([x,y,z])
                elif z==0 and graph[x][y] == 1 and visited[x][y][z+1] == -1 :
                    visited[x][y][z+1] = visited[a][b][z] +1
                    queue.append([x,y,z+1])
            
n, m = map(int,sys.stdin.readline().split())
graph =  [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
queue = deque()
visited = [[[-1]*2 for _ in range(m)] for _ in range(n)]

bfs()
      
cnt1, cnt2 = visited[n-1][m-1][0], visited[n-1][m-1][1]

if cnt1 != -1 and cnt2 == -1:
    print(cnt1)
elif cnt1 == -1 and cnt2 != -1:
    print(cnt2)
else :
    print(min(cnt1, cnt2))
