import sys
from collections import deque
input = sys.stdin.readline


dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    while deq:
        a, b = deq.popleft()
        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if 0<=x<r and 0<=y<c:
                if farm[x][y] == '.':
                    farm[x][y] = 'D'
                elif farm[x][y] == 'S':
                    return 0
    return [1,farm]
    

r,c = map(int,input().split())
farm = [list(input().strip()) for _ in range(r)]

deq = deque()

for i in range(r):
    for j in range(c):
        if farm[i][j] == 'W':
            deq.append([i,j])
if not deq:
    print(1)
    for f in farm:
        print(''.join(map(str,f)))
else:
    if not bfs():
        print(0)
    else:
        answer, farm = bfs()
        print(answer)
        for f in farm:
            print(''.join(map(str,f)))
        