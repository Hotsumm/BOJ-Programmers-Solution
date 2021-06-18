def check(s,temp):
    for arr in s:
        if arr == '(' or arr == '{' or arr == '[':
            temp.append(arr)
        elif arr == ')':
            if temp and temp[-1] == '(':
                temp.pop()
            else: return False
        elif arr == '}':
            if temp and temp[-1] == '{':
                temp.pop()
            else: return False
        elif arr == ']':
            if temp and temp[-1] == '[':
                temp.pop()
            else: return False
            
    if not temp : return True
    else : return False

def solution(s):
    answer = 0
    for i in range(len(s)):
        if i != 0:
            left = s[0]
            s = s[1:] + left
        if check(s,[]):
            answer += 1

    return answer

print(solution("[](){}"))
