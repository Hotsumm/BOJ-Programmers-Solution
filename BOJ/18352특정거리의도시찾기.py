import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    deq = deque()
    deq.append([x,0])
    while deq:
        idx,cnt = deq.popleft()
        if cnt == k:
            if idx != x:
                answer.append(idx)
                continue
        for city in graph[idx]:
            if not visited[city]:
                deq.append([city,cnt+1])
                visited[city] = 1

    

n,m,k,x = map(int,input().split())
graph = [[] for i in range(n+1)]
answer= []
visited= [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

bfs(x)

if not answer:
    print(-1)
else:
    answer.sort()
    for num in answer:
        print(num)
        