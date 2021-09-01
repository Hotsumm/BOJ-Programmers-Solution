import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance[start] = 0
    heap = []
    heapq.heappush(heap,(0,start))
    
    while heap:
        dist, curr = heapq.heappop(heap)
        if distance[curr] < dist:
            continue
        
        for g in graph[curr]:
            cost = dist + g[1]
            if cost < distance[g[0]]:
                distance[g[0]] = cost
                heapq.heappush(heap,(cost,g[0]))
            
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, c = map(int,input().split())
    graph[x].append((y,c))

start, end = map(int,input().split())

dijkstra(start)

print(distance[end])
    