import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)


def dijkstra(x,distance):
    heap = []
    distance[x] = 0
    heapq.heappush(heap,[0,x])
    while heap:
        dist, curr = heapq.heappop(heap)
        if  distance[curr] < dist :
            continue
        
        for g in graph[curr]:
            cost = dist + g[1]
            if cost < distance[g[0]]:
                distance[g[0]] = cost
                heapq.heappush(heap,[cost,g[0]])
    
n,m,x = map(int,input().split())

graph = [[] for _ in range(m+1)]
distance = [INF] * (n+1)
distance[0] = 0

for _ in range(m):
    s, e, t = map(int,input().split())
    graph[s].append([e,t])

dijkstra(x,distance)


for i in range(1,n+1):
    temp = [INF] * (n+1)
    dijkstra(i,temp)
    distance[i] += temp[x]
answer = max(distance)
print(answer)
