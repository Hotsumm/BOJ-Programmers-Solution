import sys
import heapq
input = sys.stdin.readline

nx = [1,-1,0,0]
ny = [0,0,1,-1]

def move(i,j):
    visited[i][j] = 1
    heap = []
    heapq.heappush(heap,[0,i,j])
    while heap:
        cnt, a, b = heapq.heappop(heap)
        if a == m-1 and b == n-1:
            return cnt
        for k in range(4):
            x = a + nx[k]
            y = b + ny[k]
            if 0<=x<m and 0<=y<n and not visited[x][y]:
                visited[x][y] = 1
                if board[x][y] == '0':
                    heapq.heappush(heap,[cnt,x,y])
                elif board[x][y] == '1':
                    heapq.heappush(heap,[cnt+1,x,y])
                
n,m = map(int,input().split()) 
board = [list(input().rstrip()) for _ in range(m)]
visited = [[0]*n for _ in range(m)]

print(move(0,0))
