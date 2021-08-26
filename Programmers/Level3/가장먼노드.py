from collections import deque

def move(n,graph,visited_cnt):
    visited = [False]*(n+1)
    deq = deque()
    deq.append([1,0])
    visited[1] = True
    
    while deq:
        node,cnt = deq.popleft()
        for nd in graph[node]:
            if not visited[nd]:
                visited[nd] = True
                visited_cnt[cnt+1] += 1
                deq.append([nd,cnt+1])
    return     

def solution(n, edges):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited_cnt = [0]*n

    for edge in edges:
        x,y = edge
        graph[x].append(y)
        graph[y].append(x)

    move(n,graph,visited_cnt)
    
    for i in range(len(visited_cnt)-1,-1,-1):
        if visited_cnt[i] != 0 :
            answer = visited_cnt[i]
            break
        
    return answer


