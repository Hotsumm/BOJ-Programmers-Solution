from collections import deque
import sys
input = sys.stdin.readline


dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    cnt = 0 
    while s:
        for _ in range(len(water)):
            a,b = water.popleft()
            for k in range(4):
                x = dx[k] + a
                y = dy[k] + b
                if 0<=x<r and 0<=y<c:
                    if visited[x][y] != 2 and (f[x][y] == '.'or f[x][y] == 'S'):
                        visited[x][y] = 2
                        f[x][y] = '*'
                        water.append([x,y])
        cnt += 1 
        for _ in range(len(s)):
            a,b = s.popleft()
            for k in range(4):
                x = dx[k] + a
                y = dy[k] + b
                if 0<=x<r and 0<=y<c:
                    if visited[x][y] == 0  and f[x][y] == '.' :
                        visited[x][y] = 1
                        f[x][y] = 'S'
                        s.append([x,y])
                    elif f[x][y] == 'D':
                        return cnt
            
    return 'KAKTUS'        
  
r,c = map(int,input().split())
visited = [[0]*c for _ in range(r)]
f = [list(input().strip()) for _ in range(r)]
s,water = deque(),deque()

for i in range(r):
    for j in range(c):
        if f[i][j] == 'S':
            s.append([i,j])
            visited[i][j] = 1
        elif f[i][j] == '*':
            water.append([i,j])
            visited[i][j] = 2
print(bfs())
