def solution(n, s):
    answer = []
    while n:
        temp = s // n
        answer.append(temp)
        s -= temp
        n -= 1
        
    if 0 in answer:
        return [-1]
    
    return answer

