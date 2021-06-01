import sys
from collections import deque
input = sys.stdin.readline


dx = [0,1,-1,0,0]
dy = [0,0,0,1,-1]

def bfs(i,j):
    deq = deque()
    deq.append([i,j])
    o,v = 0,0
    while deq:
        a, b = deq.popleft()
        for k in range(5):
            x = dx[k] + a
            y = dy[k] + b
            if 0<=x<r and 0<=y<c and not visited[x][y]:
                if garden[x][y] != '#':
                    if garden[x][y] == 'o':
                        o += 1
                    elif garden[x][y] == 'v':
                        v += 1
                    visited[x][y] = 1
                    deq.append([x,y])
    if v>=o:
        return [0,v]
    elif v<o:
        return [o,0]
                    
                    
                
    

r,c = map(int,input().split())
garden = [list(input().strip()) for _ in range(r)]
visited = [[0]*c for _ in range(r)]

sheep,wolf = 0,0
for i in range(r):
    for j in range(c):
        if garden[i][j] == 'v' or garden[i][j] == 'o':
            o,v = bfs(i,j)
            sheep += o
            wolf += v
print(sheep,wolf)
