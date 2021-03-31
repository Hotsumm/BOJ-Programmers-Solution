dx = [1,-1,0,0]
dy = [0,0,1,-1]            

def bfs(i,j):
    queue = [[i,j]]
    square[i][j] = 0
    cnt = 1
    while queue:
        a,b = queue[0][0],queue[0][1]
        del queue[0]
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0<=x<n and 0<=y<n and square[x][y] == 1:
                square[x][y] = 0
                queue.append([x,y])
                cnt += 1
        if len(queue)==0:
            cnt_list.append(cnt)
n = int(input())
square = list()
cnt_list = list()
for _ in range(n):
    square.append(list(map(int,input())))
for i in range(n):
    for j in range(n):
        if square[i][j] == 1:
            bfs(i,j)
            
print(len(cnt_list))
if len(cnt_list)!=0:
    cnt_list.sort()
    for i in range(len(cnt_list)):
        print(cnt_list[i])
else:
    print(0)
