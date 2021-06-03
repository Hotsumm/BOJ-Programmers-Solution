import sys
from collections import deque
input = sys.stdin.readline


a,b,n,m = map(int,input().split())
jump = [-1,1,-a,a,-b,b,a,b]
answer = 0
visited = [0]*100001
deq = deque()
deq.append([n,0])

while deq:
    curr,cnt = deq.popleft()
    if curr == m:
        answer = cnt
        break
    for k in range(8):
        temp = 0
        if k >=6:
            temp = jump[k]*curr
        else:
            temp = jump[k] + curr
        if 0<=temp<100001 and not visited[temp] :
            visited[temp] = 1
            deq.append([temp,cnt+1])
print(answer)
        
    
