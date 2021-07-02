def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    numbers = sorted(numbers,key=lambda x:int((x*4)[:4]),reverse=True)
    answer = str(int(''.join(numbers)))
    
    return answer




