import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(i,j):
    c = deque()
    deq = deque()
    deq.append([i,j])
    sum_p = 0
    cnt = 0
    while deq:
        a,b = deq.popleft()
        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if 0<=x<n and 0<=y<n and not visited[x][y]:
                if l<=abs(people[a][b]-people[x][y])<=r and [x,y] not in c:
                    deq.append([x,y])
                    visited[x][y] = 1
                    c.append([x,y])
                    cnt += 1
                    sum_p += people[x][y]
    if not cnt :
        return 0
    
    while c:
        a,b = c.popleft()
        people[a][b] = sum_p//cnt
    return 1

                  

n,l,r = map(int,input().split())
people = [list(map(int,input().split())) for _ in range(n)]
answer = 0

while True:
    visited = [[0]*n for _ in range(n)]
    check = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                check += bfs(i,j)
    if not check:
        break
    answer += 1 
print(answer)

        

