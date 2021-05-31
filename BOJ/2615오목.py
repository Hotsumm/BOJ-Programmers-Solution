import sys
input = sys.stdin.readline

dx = [-1,0,1,1]
dy = [1,1,1,0]

def bfs():
    for i in range(19):
        for j in range(19):
            if board[i][j] == 1:
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    cnt = 1
                    while 0<=x<19 and 0<=y<19 and board[x][y]==1:
                        x += dx[k]
                        y += dy[k]
                        cnt +=1
                    if cnt == 5:
                        x = i-dx[k]
                        y = j-dy[k]
                        if 0<=x<19 and 0<=y<19 and board[x][y] == 1:
                            break
                        else:
                            return 1,i+1,j+1
            elif board[i][j] == 2:
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    cnt = 1
                    while 0<=x<19 and 0<=y<19 and board[x][y]==2:
                        x += dx[k]
                        y += dy[k]
                        cnt +=1
                    if cnt == 5:
                        x = i-dx[k]
                        y = j-dy[k]
                        if 0<=x<19 and 0<=y<19 and board[x][y] == 2:
                            break
                        else:
                            return 2,i+1,j+1
                    
    return 0,0,0 
board = [list(map(int,input().split())) for _ in range(19)]

result,w,l = bfs()
if result:
    print(result)
    print(w,l)
else:
    print(result)
