import heapq

def solution(n, works):
    answer = 0
    heap = []
    heapq.heapify(heap)
    for work in works:
        heapq.heappush(heap,-work)
    
    while n != 0:
        temp = -heapq.heappop(heap)
        if temp ==0:
            heapq.heappush(heap,temp)
            break
        temp -= 1
        n -= 1
        heapq.heappush(heap,-temp)
         
            
    for _ in range(len(works)):
        answer +=  (-heapq.heappop(heap)) ** 2
        
    return answer

