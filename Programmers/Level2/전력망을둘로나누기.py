from collections import deque

def bfs(a,graph,visited):
    count = 1
    deq = deque()
    deq.append(a)
    visited[a] = 1
    while deq:
        curr = deq.popleft()
        for _next in graph[curr]:
            if not visited[_next]:
                count += 1
                visited[_next] = 1
                deq.append(_next)   
    return count
   
def solution(n, wires):
    answer = 99
    graph = [[] for _ in range(n+1)]
    
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for a,b in wires: 
        visited = [0] * (n+1)
        visited[b]= 1
        result = bfs(a,graph,visited)
        _abs = abs((result*2) - n )
        answer = min(answer, _abs)
        
    return answer
