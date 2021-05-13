# List보다 tuple이 가벼움 
# deq List추가(시간초과)
import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]
h_dx = [2,1,-2,-1,1,-1,-2,2]
h_dy = [1,2,-1,-2,-2,2,1,-1]


def bfs(i,j,k):
    visited[i][j][k] = 1
    deq.append((i,j,k))
    while deq:
        nx,ny,k= deq.popleft()
        if nx == h-1 and ny == w-1:
            return visited[nx][ny][k]-1
        for l in range(4):
            x = dx[l] + nx
            y = dy[l] + ny
            if 0<=x<h and 0<=y<w :
                if board[x][y] == 0 and not visited[x][y][k]:
                    visited[x][y][k] =  visited[nx][ny][k] + 1
                    deq.append((x,y,k))
        if k > 0:
            for l in range(8):
                x = h_dx[l] + nx
                y = h_dy[l] + ny
                if 0<=x<h and 0<=y<w:
                    if board[x][y] == 0 and not visited[x][y][k-1]:
                        visited[x][y][k-1] =  visited[nx][ny][k] + 1
                        deq.append((x,y,k-1))
                
    return -1

k = int(input())
w,h = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(h)]
visited = [[[0] * (k+1) for _ in range(w)] for _ in range(h)]
deq = deque()
print(bfs(0,0,k))

