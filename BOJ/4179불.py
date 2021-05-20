import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0] 
dy = [0,0,1,-1]

def bfs():
    cnt = 0
    while move:
        cnt += 1                    
        for _ in range(len(move)):
            mx, my = move.popleft()
            if maze[mx][my] == 'F':
                continue
            if mx == 0 or mx == r-1 or my == 0 or my == c-1:
                if maze[mx][my] == 'J':
                    return cnt
            for k in range(4):
                x = dx[k] + mx
                y = dy[k] + my
                if 0<=x<r and 0<=y<c and maze[x][y] == '.' :
                    move.append([x,y])
                    maze[x][y] = 'J'
                    
        for _ in range(len(fire)):
            fx, fy = fire.popleft()
            for k in range(4):
                x = dx[k] + fx
                y = dy[k] + fy
                if 0<=x<r and 0<=y<c :
                    if maze[x][y] == '.' or maze[x][y] == 'J':
                        maze[x][y] = 'F'
                        fire.append([x,y])
    return "IMPOSSIBLE"


r,c = map(int,input().split())
maze = [list(input().strip()) for _ in range(r)]

move, fire= deque(),deque()

for i in range(r):
    for j in range(c):
        if maze[i][j] == 'J':
            move.append([i,j])
        elif maze[i][j] == 'F':
            fire.append([i,j])
print(bfs())
