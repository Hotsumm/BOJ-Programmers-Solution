from collections import deque
import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def melt():
    while water:
        a,b = water.popleft()
        if lake[a][b] == 'X':
            lake[a][b] = '.'
        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if 0<=x<r and 0<=y<c and not visited_w[x][y]:
                if lake[x][y]=='X' :
                    next_water.append([x,y])
                visited_w[x][y] = 1
                      
def bfs():
    while sw:
        a,b = sw.popleft()
        if a == tx and b == ty:
            return True
        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if 0<=x<r and 0<=y<c and not visited_s[x][y]:
                visited_s[x][y] = 1
                if lake[x][y] == 'X':
                    next_sw.append([x,y])
                elif lake[x][y] == '.':
                    sw.append([x,y])
                visited_s[x][y] = 1
    return False

r,c = map(int,input().split())

visited_w,visited_s = [[0]*c for _ in range(r)],[[0]*c for _ in range(r)]  # 물, 백조 방문기록

lake = [list(input().rstrip()) for _ in range(r)]
water,next_water,sw,next_sw = deque(),deque(),deque(),deque()  
tx,ty = 0, 0  

for i in range(r):
    for j in range(c):
        if lake[i][j] == 'L':
            if not sw:      
                sw.append([i,j]) #시작 백조
            else:
                tx,ty = i,j #최종 만나야할 백조
            lake[i][j] = '.'
            
        if lake[i][j] == '.':
            water.append([i,j])

answer = 0

while True:
    melt()
    if bfs():
        print(answer)
        break
    water = next_water  # 다음 빙판 ->물로 변할 곳
    next_water = deque()  
    sw = next_sw # 다음 백조가 이동할 수 있는 곳
    next_sw = deque()
    answer += 1
    
