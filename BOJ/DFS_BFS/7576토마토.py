import sys
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]            
day_list = list()
check = True

def bfs():
    day = -1
    while queue:
        for _ in range(len(queue)):
            a,b = queue.popleft()
            for k in range(4):
                x = a + dx[k]
                y = b + dy[k]
                if 0<=x<n and 0<=y<m and box[x][y] == 0 :
                    box[x][y] = 1
                    queue.append([x,y])
        day += 1
    day_list.append(day)
            
m,n = map(int,sys.stdin.readline().split())
box = []
queue = deque()

for i in range(n):
    box.append(list(map(int,sys.stdin.readline().split())))
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i,j])
bfs()
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            check = False
if check:
    print(sum(day_list))
else :
    print(-1)
