import sys
import heapq
input = sys.stdin.readline

n = int(input())
min_h,max_h = [],[]

for _ in range(n):
    num = int(input())
   
    if len(min_h) == len(max_h):
        heapq.heappush(max_h,-num)
    else:
        heapq.heappush(min_h,num)

    if len(min_h) > 0 and len(max_h) > 0:
        if min_h[0] < -max_h[0]:
            max_v = -(heapq.heappop(max_h))
            min_v = heapq.heappop(min_h)
            heapq.heappush(min_h,max_v)
            heapq.heappush(max_h,-min_v)

    print(-max_h[0])
