from collections import deque
import sys
def bfs(n,k):
    deq = deque()
    deq.append(n)
    while deq:
        t = deq.popleft()
        if t == k:
            return time[t]
        for move in [t+1,t-1,2*t]:
            if 0<= move < 100001 and time[move]== 0 :
                time[move] = time[t] + 1
                deq.append(move)
        
n,k = map(int,sys.stdin.readline().split())
time = [0] * 100001
print(bfs(n,k))
