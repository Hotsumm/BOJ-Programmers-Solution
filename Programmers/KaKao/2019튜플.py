def solution(s):
    answer = []

    s = s[2:-2].split("},{")
    s = sorted(s,key=len)
    for i in s :
        numbers = (list(map(int,i.split(','))))
        for number in numbers:
            if number not in answer:
                answer.append(number)
    
    return answer
