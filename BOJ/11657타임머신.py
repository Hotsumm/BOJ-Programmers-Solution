import sys
input = sys.stdin.readline

INF = int(1e9)

def bellman_ford(start):
    dist[start] = 0

    for i in range(n):
        for j in range(m):
            curr, _next, cost = edges[j][0],edges[j][1], edges[j][2]
            if dist[curr] != INF and dist[_next] > cost + dist[curr]:
                dist[_next] =  cost + dist[curr]
                if i == n-1:
                    return True
    return False

n,m = map(int,input().split())
dist = [INF]*(n+1) 
edges = []
is_cycle = False

for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))

is_cycle = bellman_ford(1)
    
if is_cycle:
    print(-1)
else:
    for i in range(2,n+1):
        if dist[i] == INF:
            print(-1)
            continue
        print(dist[i])
    
