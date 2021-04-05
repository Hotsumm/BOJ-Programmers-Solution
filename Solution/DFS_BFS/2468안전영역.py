import sys 
n = int(sys.stdin.readline())
area = []
cnt_list = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i,j):
    queue = [[i,j]]
    while queue:
        a,b = queue[0][0],queue[0][1]
        del queue[0]
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0<=x<n and 0<=y<n and copy[x][y]==1:
                copy[x][y] = 0
                queue.append([x,y])  

for i in range(n):
    area.append(list(map(int,sys.stdin.readline().split())))

max_num = max(map(max, area))

for l in range(1,max_num+1):
    copy = [[0]*n for i in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if area[i][j]-l >= 0:
                copy[i][j] = 1
    for i in range(n):
        for j in range(n):
            if copy[i][j] == 1:
                bfs(i,j)
                cnt += 1
    cnt_list.append(cnt)
print(max(cnt_list))


