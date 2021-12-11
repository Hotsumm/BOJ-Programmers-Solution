import math

def solution(n, stations, w):
    answer = 0

    curr = 1
    _range = 2*w + 1

    for station in stations:
        temp = station - w - curr
        if temp > 0 :
            answer += math.ceil(temp/_range)
        curr = station + w + 1
        
    if n >= curr:
        answer += math.ceil((n-curr+1)/_range) 
    
    return answer

