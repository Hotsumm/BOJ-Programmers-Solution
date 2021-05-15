# set을 사용하지않고 중복없이 더 좋은코드로 다시풀기
import sys
input = sys.stdin.readline
def dfs(i,v):
    visited[i] = 1
    if visited[v] == 0:
        dfs(v,board[v])
    elif visited[v]==1 and  v == board[i] :
        answer.append(v)
n = int(input())

board = [0]*(n+1)
answer= []

for i in range(1,n+1):
    board[i] =int(input())
    
for i in range(1,n+1):
    visited = [0]*(n+1)
    dfs(i,board[i])
answer = list(set(answer))
answer.sort()
print(len(answer))
for item in answer:
    print(item)
