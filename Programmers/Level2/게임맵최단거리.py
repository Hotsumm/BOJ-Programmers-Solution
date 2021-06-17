from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def move(i,j,maps):
    n, m= len(maps),len(maps[0])
    visited = [[0]*m for _ in range(n)]
    deq = deque()
    deq.append([i,j,1])
    
    while deq:
        a,b,cnt = deq.popleft()
        if a == n-1 and b == m-1:
            return cnt
        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if 0<=x<n and 0<=y<m:
                if maps[x][y] == 1 and not visited[x][y]:
                    visited[x][y] = 1
                    deq.append([x,y,cnt+1])
    return -1            
                
    
def solution(maps):
    answer = move(0,0,maps)   
    return answer


