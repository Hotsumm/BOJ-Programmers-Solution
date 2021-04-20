def solution(number, k):
    answer = ''
    stack = []
    
    for idx,num in enumerate(number):
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        if k == 0 :
            stack += number[idx:]
            break
        
        stack.append(num)
        
    if k>0:
        answer = "".join(stack[:-k])
        return answer
    
    answer = "".join(stack)
    return answer



