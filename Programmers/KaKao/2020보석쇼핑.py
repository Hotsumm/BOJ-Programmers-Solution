def solution(gems):
    answer = []
    n = len(set(gems))
    start, end = 0, 0
    jewelry = {}

   
    while end < len(gems):
        if gems[end] not in jewelry:
            jewelry[gems[end]] = 1
        else:
            jewelry[gems[end]] += 1

        end += 1
        
        if n == len(jewelry):
            while start < end:
                if jewelry[gems[start]] > 1:
                    jewelry[gems[start]] -= 1
                    start += 1
                else:
                    if not answer:
                        answer = [start+1,end]
                    else:            
                        if answer[1] - answer[0] > end - (start+1):
                            answer = [start+1,end]
                        elif answer[1] - answer[0] == end - (start+1):
                            if answer[0] > start+1:
                                answer = [start+1,end]
                        
                    break
    return answer


