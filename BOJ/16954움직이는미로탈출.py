import sys
from collections import deque
input = sys.stdin.readline

dx = [0,1,-1,1,-1,1,-1,0,0]
dy = [0,1,-1,-1,1,0,0,1,-1]

def bfs(i,j,wall):
    deq = deque()
    deq.append([i,j])
    while deq:
        visited = [[0]*8 for _ in range(8)]
        for _ in range(len(deq)):
            nx,ny = deq.popleft()
            if nx == 0 and ny == 7:
                return 1
            
            if board[nx][ny] == '#':
                continue
           
            for k in range(9):
                x = dx[k] + nx
                y = dy[k] + ny
                if 0<=x<8 and 0<=y<8:
                    if not visited[x][y] and board[x][y] == '.':
                        visited[x][y] = 1
                        deq.append([x,y])
        board.pop()
        board.insert(0, ['.', '.', '.', '.', '.', '.', '.', '.'])   

    return 0


board = [list(input().strip()) for _ in range(8)]
wall = []
for i in range(8):
    for j in range(8):
        if board[i][j] == '#':
            wall.append([i,j])

print(bfs(7,0,wall))

