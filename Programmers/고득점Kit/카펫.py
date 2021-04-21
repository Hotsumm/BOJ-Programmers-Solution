def solution(brown, yellow):
    answer = []
    area = brown + yellow

    for i in range(area-1,3, -1):
        if area % i == 0:
            h = area // i
            
            if yellow == (h-2)*(i-2) :
                answer.append(i)
                answer.append(h)
                break
        
    return answer

