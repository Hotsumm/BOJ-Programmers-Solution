import sys
input = sys.stdin.readline

INF = int(1e9)

def floyd():
    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                dist[a][b] = min(dist[a][b],dist[a][k]+dist[k][b])

n = int(input())
m = int(input())

dist = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    dist[a][b] = min(dist[a][b], c)

floyd()

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j or dist[i][j] ==INF:
            print(0, end=" ")
            continue
        print(dist[i][j], end=" ")
    print()
