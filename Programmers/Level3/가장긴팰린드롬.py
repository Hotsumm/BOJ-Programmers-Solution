def reverse(s):
    return s[::-1]

def solution(s):
    answer = 0
    if len(s) == 1 :
        return 1
    
    for i in range(len(s)-1):
        for j in range(i+1,len(s)+1):
            if s[i:j] == reverse(s[i:j]):
                answer = max(answer,len(s[i:j]))
    return answer 

