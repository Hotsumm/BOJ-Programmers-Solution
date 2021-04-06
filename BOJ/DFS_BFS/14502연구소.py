from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    while queue:
        a,b = queue.popleft()
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0<=x<n and 0<=y<m and lab[x][y] == 0 :
                lab[x][y] = 2
                queue.append([x,y])

n, m = map(int,input().split())
queue = deque()
empty = []
lab = []
virus_list = []

for i in range(n):
    lab.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if lab[i][j] == 2:
            queue.append([i,j])
        elif lab[i][j] == 0:
            empty.append([i,j])       
bfs()

