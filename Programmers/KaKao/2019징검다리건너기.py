def solution(stones, k):
    left = 1
    right = max(stones)
    answer = 0
    
    while left<= right:
        cnt = 0
        mid = (left+right) // 2
        for stone in stones:
            if stone - mid <= 0:
                cnt += 1
            else :
                cnt = 0
            if cnt >= k :
                answer = mid
                right = mid - 1
                break
        if cnt < k:
            left = mid + 1
    
    return answer

