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
            if 0<=x<n and 0<=y<n and paint[a][b] == paint[x][y] and copy[x][y] == 0:
                copy[a][b] = 1
                copy[x][y] = 1
                queue.append([x,y])

n = int(input())     
paint = []
cnt = 0

for _ in range(n):
    paint.append(list(input()))
    
copy = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if copy[i][j] != 1:
            cnt += 1
            bfs(i,j)
print(cnt,end =' ')

copy = [[0]*n for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(n):
        if paint[i][j] == 'R':
            paint[i][j] = 'G'
            
for i in range(n):
    for j in range(n):
        if copy[i][j] != 1:
            cnt +=1
            bfs(i,j)
print(cnt)     
        
