import heapq

def change(heap):
    h = []
    for i in range(len(heap)):
        heapq.heappush(h,-heap[i])
    return h

def solution(operations):
    answer = []
    heap = []
    
    for operation in operations:
        op1,op2 = operation.split()
        op2 = int(op2)
        if op1 == 'I':
            heapq.heappush(heap,op2)
        else:
            if not heap : continue
            
            if op2 == 1:
                heap = change(heap)
                heapq.heappop(heap)
                heap = change(heap)              
            else:
                heapq.heappop(heap)
                
    if not heap:
        answer += [0,0]
    else :
        _min = heapq.heappop(heap)
        heap = change(heap)
        _max = -heapq.heappop(heap)
        answer += [_max,_min]

    
    return answer


