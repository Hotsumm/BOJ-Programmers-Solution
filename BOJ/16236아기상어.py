from collections import deque
import sys
import heapq
input = sys.stdin.readline


dx = [1,-1,0,0]
dy = [0,0,1,-1]

def move(i,j):
    visited[i][j] = 1
    heap = []
    deq = deque()
    deq.append([0,i,j])
    while deq:
        time,nx,ny = deq.popleft()
        for k in range(4):
            x = dx[k] + nx
            y = dy[k] + ny
            if 0<=x<n and 0<=y<n and not visited[x][y]:
                visited[x][y] = 1
                if space[x][y] == 0 or space[x][y] == size:
                    deq.append([time+1,x,y])
                elif space[x][y] < size and space[x][y] != 0:
                     heapq.heappush(heap,[time+1,x,y])
    if heap:
        return heap[0]
    else:
        return None

n = int(input())
space = [list(map(int,input().split())) for _ in range(n)]
s1,s2= 0,0
food = 0
cnt,size = 0,2
answer= 0
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            s1,s2 = i,j
            space[i][j] = 0
        elif 0<space[i][j]<=6:
            food += 1
    
while food != 0:
    visited = [[0]*n for _ in range(n)]
    result = move(s1,s2)
    if result != None:
        answer += result[0]
        s1,s2 =result[1],result[2]
        space[s1][s2] = 0
        cnt += 1
        if cnt == size:
            cnt = 0
            size += 1 
    else:
        break
print(answer)

