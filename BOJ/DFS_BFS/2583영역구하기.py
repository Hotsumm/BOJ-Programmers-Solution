dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i,j):
    queue= [[i,j]]
    cnt = 1
    while queue:
        a,b = queue[0][0],queue[0][1]
        del queue[0]
        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if 0<=x<m and 0<=y<n and square[x][y]==0:
                cnt +=1
                square[x][y] = 1
                queue.append([x,y])
                
    cnt_list.append(cnt)
    
m,n,k = map(int,input().split())
location = []
cnt_list = []

for _ in range(k):
    location.append(list(map(int,input().split())))

square = [[0]*n for i in range(m)]

for k in range(len(location)):
    coord = location[k]
    for i in range(coord[1],coord[3]):
        for j in range(coord[0],coord[2]):
            if square[i][j]==0:
                square[i][j] = 1
for i in range(m):
    for j in range(n):
        if square[i][j] == 0:
            square[i][j] = 1 
            bfs(i,j)

cnt_list.sort()
print(len(cnt_list))
for i in range(len(cnt_list)):
    print(cnt_list[i],end=" ")


    
