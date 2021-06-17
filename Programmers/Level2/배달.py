from collections import deque

def bfs(N,K,city,visited):
    possible = [1]
    visited[1] = 1
    deq = deque()
    deq.append([1,K,0])
    while deq:
        i,k,t = deq.popleft()
        for j in range(1,N+1):  
            if (not visited[j] or t+city[i][j] < visited[j] ) and city[i][j] != 0:
                if k-city[i][j] >= 0:
                    deq.append([j,k-city[i][j],t+city[i][j]])
                    visited[j] = t+city[i][j]
                    if j not in possible :
                        possible.append(j)
    return len(possible)
            
def solution(N, road, K):
    visited = [0]*(N+1)
    city = [[0]*(N+1) for _ in range(N+1)]
    for r in road:
        a,b,d = r
        if city[a][b] != 0 or city[b][a] != 0 :
            city[a][b] = min(city[a][b],d)
            city[b][a] = min(city[b][a],d)
        else:
            city[a][b] = d
            city[b][a] = d
    answer = bfs(N,K,city,visited)

    
    return answer




