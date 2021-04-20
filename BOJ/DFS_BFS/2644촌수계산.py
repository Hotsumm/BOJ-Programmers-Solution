import sys
n = int(sys.stdin.readline())
a,b = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())

def bfs(a,b):
    cnt = 0 
    visited[a] = 1
    queue = [a]
    v = 0
    while queue:
        for k in range(len(queue)):
            v = queue[0]
            if v == b:
                return cnt
            visited[v] = 1
            del queue[0]
            for i in range(1,n+1):
                if visited[i]==0 and graph[v][i]==1:
                    queue.append(i)
        cnt += 1
    return -1

visited = [0]*(n+1)
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1
print(bfs(a,b))

    

