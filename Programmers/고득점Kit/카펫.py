def solution(brown, yellow):
    answer = []
    area = brown + yellow

    for i in range(area,2, -1):
        if area % i == 0:
            h = area // i
            if yellow == (h-2)*(i-2) :
                answer = [i,h]
                break
                
    return answer

