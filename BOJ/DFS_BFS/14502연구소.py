from collections import deque
from itertools import combinations
import copy
import sys
dx = [-1,1,0,0]
dy = [0,0,1,-1]


def bfs():
    cnt = 0
    deq = deque()
    for i,j in virus:
        deq.append([i,j])
    while deq:
        x,y = deq.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==0 and copy_graph[nx][ny] == 0:    
                    copy_graph[nx][ny] = 2 
                    deq.append([nx,ny])
                    cnt +=1
    return cnt
    
    
n,m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
empty = []
virus = []
safety = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty.append((i,j))
        elif graph[i][j] == 2:
            virus.append([i,j])
combi = list(combinations(empty,3))

for c in combi:
    cnt = 0
    copy_graph = copy.deepcopy(graph)
    for a,b in c :
        copy_graph[a][b] = 1
    bfs()
    for r in copy_graph:
        cnt += r.count(0)
    safety = max(safety,cnt)
    
print(safety)
