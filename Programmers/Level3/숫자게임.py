from collections import deque

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    B = deque(B)
    
    for a in A:
        while B:
            temp = B.popleft()
            if a<temp:
                answer += 1
                break

    return answer
