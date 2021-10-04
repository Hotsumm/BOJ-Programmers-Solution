def solution(a):
    answer = 0
    reverse_a = list(reversed(a))
    
    left_list = []
    right_list = []
    _min = 1000000000
    
    for bl in a:
        _min = min(_min,bl)
        left_list.append(_min)
        
    _min = 1000000000
    for bl in reverse_a:
        _min =  min(_min,bl)
        right_list.append(_min)  

    right_list.reverse()    

    for idx,bl in enumerate(a):
        if idx == 0 or idx == len(a)-1:
            answer += 1
            continue
        if left_list[idx]>=bl or right_list[idx]>=bl:
            answer += 1    
    return answer

