from collections import deque
import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def puyo(i,j,target):
    chain.append([i,j])
    visited[i][j] = 1
    deq.append([i,j])
    while deq:
        a,b = deq.popleft()
        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if 0<=x<6 and 0<=y<12:
                if not visited[x][y] and target == field[x][y]:
                    deq.append([x,y])
                    visited[x][y] = 1
                    chain.append([x,y])

    if len(chain) >=4 :
        for x,y in chain:
            field[x][y] = 0
        return 1
    return 0

def drop():
    n = 0
    for i in range(6):
        n = field[i].count(0)
        if n>0:
            for _ in range(n):
                field[i].remove(0)
                field[i].append('.')
            
field = [list(input().strip()) for _ in range(12)]
field.reverse()
field = list(map(list,zip(*field)))

answer = 0
deq = deque()
while True:
    check = 0
    visited = [[0]*12 for _ in range(6)]
    for i in range(6):
        for j in range(12):
            if field[i][j] != '.' and not visited[i][j] :
                chain = []
                check += puyo(i,j,field[i][j])
    if check>0:
        answer += 1
        drop()
    else: break

print(answer)  
