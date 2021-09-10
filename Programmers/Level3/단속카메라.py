def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x:x[1])
    end = 0
    for i,route in enumerate(routes):
        if i == 0 :
            end = route[1]
            answer += 1
            continue
        
        if end < route[0]:
            answer += 1
            end = max(end,route[1])
            
    return answer
