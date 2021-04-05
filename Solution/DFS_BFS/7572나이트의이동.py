dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1,1,2,2,1,-1,-2]

def bfs(i,j):
    queue = [[i,j]]
    cnt = 0
    while queue:
        for _ in range(len(queue)):
            a,b = queue[0][0],queue[0][1]
            del queue[0]
            for k in range(8):
                x = a + dx[k]
                y = b + dy[k]
                if 0<=x<l and 0<=y<l and board[x][y]==0:
                    board[x][y] = 1
                    queue.append([x,y])
                    if x == end_x and y == end_y:
                        print(cnt+1)
                        return
        cnt += 1          
        
t = int(input())

for _ in range(t):
    check = True
    cnt_list = []
    l = int(input())
    board = [[0]*l for _ in range(l)]
    start_x, start_y = map(int,input().split())
    end_x,end_y = map(int,input().split())
    if start_x == end_x and start_y == end_y:
        print(0)
    else :
        bfs(start_x, start_y)
   
        
