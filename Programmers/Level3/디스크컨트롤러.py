import heapq

def solution(jobs):
    answer = 0
    jobs.sort()
    end = -1
    heap = []
    cnt = 0
    curr = 0
    while cnt < len(jobs):
        for job in jobs:
            start,time = job
            if end < start <= curr :
                heapq.heappush(heap,[time,start])
                
        if heap:            
            time,start = heapq.heappop(heap)
            end = curr
            curr += time
            answer += (curr - start)
            cnt += 1
        else:
            curr += 1


    answer = int(answer/len(jobs))
    
    return answer


print(solution([[0, 3], [1, 9], [2, 6]]))



 
