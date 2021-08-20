import sys
from collections import deque
sys.setrecursionlimit(100001)

def bfs(v):
    queue = deque()
    visited[v] = 1 
    queue.append(v)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] ==0 :
                visited[i] = v
                queue.append(i)
            
n = int(sys.stdin.readline())
visited = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
bfs(1)
for i in range(2,n+1):
    print(visited[i])



