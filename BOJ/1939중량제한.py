import sys
from collections import deque
input = sys.stdin.readline


def bfs(weight):
    visited[start] = 1
    deq = deque()
    deq.append(start)
    while deq:
        x = deq.popleft()
        for y,c in graph[x]:
            if not visited[y] and c>=weight :
                visited[y] = 1
                deq.append(y)
    return True if visited[end] else False

    
n,m = map(int,input().split())
graph = [[]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

start, end = map(int,input().split())

_min, _max = 1, 1000000000
answer = _min

while _min <= _max:
    visited = [0]*(n+1)
    mid = (_min + _max) // 2
    if bfs(mid):
        answer = mid
        _min = mid + 1
    else:
        _max = mid - 1
print(answer)


    
