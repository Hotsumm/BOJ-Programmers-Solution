import sys

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(i,j,cnt):
    global max_cnt
    
    max_cnt = max(cnt,max_cnt)
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if 0<=x<r and 0<=y<c and  visited[ord(board[x][y])-65] == 0:
                visited[ord(board[x][y])-65] = 1
                dfs(x,y,cnt+1)
                visited[ord(board[x][y])-65] = 0
        
    
r,c = map(int,sys.stdin.readline().split())
board = []

for _ in range(r):
    board.append(list(sys.stdin.readline()))
visited = [0] * 26
visited[ord(board[0][0])-65] = 1
max_cnt = 1

dfs(0,0,1)
print(max_cnt)
    