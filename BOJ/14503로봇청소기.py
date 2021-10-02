from collections import deque
import sys
input = sys.stdin.readline

go = {0:[-1,0],1:[0,1],2:[1,0],3:[0,-1]}
back = {0:[1,0],1:[0,-1],2:[-1,0],3:[0,1]}

def bfs(r,c):
    deq = deque()
    deq.append([r,c,d,1])
    visited[r][c] = 1
    while deq:
        b,a,_dt,cnt = deq.popleft()
        move = False
        dt = _dt
        for _ in range(4):
            if dt == 0:
                dt = 3
            else:
                dt -= 1
            my,mx = go[dt]
            x = mx + a
            y = my + b
            if 0<=y<n and 0<=x<m and not visited[y][x]:
                if not board[y][x]:
                    deq.append([y,x,dt,cnt+1])
                    visited[y][x] = 1
                    move = True
                    break
            
        if not move:
            my,mx = back[_dt]
            x = mx + a
            y = my + b
            if 0<=y<n and 0<=x<m :
                if not board[y][x]:
                    if not visited[y][x]:
                        visited[y][x] = 1
                        deq.append([y,x,_dt,cnt+1])
                        continue
                    deq.append([y,x,_dt,cnt])
                else:              
                    return cnt

n,m = map(int,input().split())
r,c,d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]


print(bfs(r,c))

