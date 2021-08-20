def solution(prices):
    answer = []
    for idx,price in enumerate(prices):
        sec = 0
        for i in range(idx+1,len(prices)):
            if price > prices[i]:
                sec += 1
                break
            sec += 1
        answer.append(sec)
    return answer
