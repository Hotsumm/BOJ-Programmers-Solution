import sys
import heapq
input = sys.stdin.readline

n = int(input())
c = []
for _ in range(n):
    c.append(list(map(int,input().split())))
c = sorted(c,key=lambda x:x[0])

heap = []
heapq.heappush(heap,c[0][1])

for i in range(1,n):
    if heap[0] > c[i][0]:
        heapq.heappush(heap,c[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap,c[i][1])
print(len(heap))
    

