import heapq

def dijkstra(s,distance,graph):
    distance[s] = 0
    heap = []
    heapq.heappush(heap,[0,s])
    
    while heap:
        dist, curr = heapq.heappop(heap)
        if distance[curr] < dist:
            continue

        for g in graph[curr]:
            cost = dist + g[1]
            if cost < distance[g[0]]:
                distance[g[0]] = cost
                heapq.heappush(heap,[cost,g[0]])
                
def solution(n, s, a, b, fares):
    answer = int(1e9)
    graph = [[] for _ in range(n+1)]
    distance = [int(1e9)] * (n+1)
    
    for fare in fares:
        f1, f2, f3 = fare
        graph[f1].append([f2,f3])
        graph[f2].append([f1,f3])
        
    dijkstra(s,distance,graph)
    
    for i in range(1,n+1):
        join = [int(1e9)] * (n+1)
        dijkstra(i,join,graph)
        temp = distance[i] + join[a] + join[b]
        if not answer :
            answer = temp
            continue
        answer = min(answer,temp)
        
    return answer

