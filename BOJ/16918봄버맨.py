import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0,0]
dy = [0,0,1,-1,0]


def bfs(n):
    full =  [['O']*c for _ in range(r)]
    if n % 2 == 0:
        return full
    for i in range(2,n+1):
        full =  [['O']*c for _ in range(r)]
        if i%2 == 0 :
            board = full
        else:
            for _ in range(len(deq)):
                a,b = deq.popleft()
                for k in range(5):
                    x = dx[k] + a
                    y = dy[k] + b
                    if 0<=x<r and 0<=y<c and board[x][y] == 'O':
                        board[x][y] = '.'
            for i in range(r):
                for j in range(c):
                    if board[i][j] == 'O':
                        deq.append([i,j])
            

    return board
                  


r, c, n= map(int,input().split())
board = [list(input().rstrip()) for _ in range(r)]
deq = deque()
for i in range(r):
    for j in range(c):
        if board[i][j] == 'O':
            deq.append([i,j])
if n == 1:
    answer = board
else:
    answer = bfs(n)
for item in answer:
    print(''.join(map(str,item)))
        