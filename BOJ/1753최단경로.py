import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

def dijkstra(start):
    distance[start] = 0
    heap = []
    heapq.heappush(heap,[0,start])
    while heap :
        dist, curr = heapq.heappop(heap)
        if distance[curr] < dist:
            continue

        for g in graph[curr]:
            cost = dist + g[1]
            if cost < distance[g[0]]:
                distance[g[0]] = cost
                heapq.heappush(heap,[cost,g[0]])
            

v, e = map(int,input().split())
start = int(input())

distance = [INF] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    x, y, c = map(int,input().split())
    graph[x].append([y,c])

dijkstra(start)

for i in range(1,v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
