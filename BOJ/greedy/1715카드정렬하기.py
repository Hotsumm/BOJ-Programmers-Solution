# 우선순위 큐
import sys
from queue import PriorityQueue
n = int(sys.stdin.readline())
pq = PriorityQueue()
for _ in range(n):
    pq.put(int(sys.stdin.readline()))
sum = 0
while pq.qsize() != 1:
    a,b = pq.get(),pq.get()
    sum += a+b
    pq.put(a+b)
print(sum)
    