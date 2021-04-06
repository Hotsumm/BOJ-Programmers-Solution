def solution(N, stages):
    answer = []
    failure = []
    for i in range(1,N+1):
        num1 = 0
        num2 = 0
        for j in stages:
            if i<j :
                num1 += 1
            elif i == j:
                num1 += 1
                num2 += 1
        if num2 == 0:
            failure.append(0)
        else :
            failure.append(num2/num1)
    for i in range(N):
        idx = failure.index(max(failure))
        answer.append(idx+1)
        failure[idx] = -1
    return answer

