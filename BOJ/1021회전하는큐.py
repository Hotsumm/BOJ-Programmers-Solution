from collections import deque
import sys
n,m = map(int,sys.stdin.readline().split())
target = list(map(int,sys.stdin.readline().split()))
deq = deque()
for i in range(1,n+1):
    deq.append(i)
    

cnt = 0 
for t in target:
    idx = deq.index(t)
    while True:
        if t == deq[0]:
            deq.popleft()
            break
        else:
            if  idx < len(deq)-idx:
                temp = deq.popleft()
                deq.append(temp)
            else:
                temp = deq.pop()
                deq.appendleft(temp)
            cnt += 1
print(cnt)
