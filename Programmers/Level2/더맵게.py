import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) >=2:
        answer += 1
        temp = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville,temp)
        if scoville[0] < K:
            continue
        break
    if scoville[0] < K:
        return -1
    return answer
print(solution([1, 2, 3, 9, 10, 12],7))
