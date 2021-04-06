from collections import deque
import sys

day = list()

def bfs():
    cnt = -1
    while queue:
        for _ in range(len(queue)):
            a,b,c = queue.popleft()
            for j in range(6):
                x = a + dx[j]
                y = b + dy[j]
                z = c + dz[j]
                if 0<=x<n and 0<=y<m and 0<=z<h and box[z][x][y] ==0:
                    queue.append([x,y,z])
                    box[z][x][y] = 1    
        cnt += 1
    day.append(cnt)

m,n,h = map(int,sys.stdin.readline().split())
check = True
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

box = [[] for i in range(h)]
queue = deque()

for k in range(h):
    for i in range(n):
        box[k].append(list(map(int,sys.stdin.readline().split())))
        for j in range(m):
            if box[k][i][j] == 1:
                queue.append([i,j,k])

bfs()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j]==0:
                check = False
if check:
    print(day[0])
else:
    print(-1)
