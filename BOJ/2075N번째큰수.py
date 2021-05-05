import heapq
import sys

heap = []
heapq.heapify(heap)
n = int(sys.stdin.readline())
min_num = 0 
for i in range(n):
    num_list = list(map(int,sys.stdin.readline().rstrip().split()))
    if i == 0:
        for num in num_list:
            heapq.heappush(heap,num)
        min_num = heap[0]
    else:
        for num in num_list:
            if min_num < num:
                heapq.heappush(heap,num)
                heapq.heappop(heap)
                min_num = heap[0]
print(heap[0])
            
            

    

