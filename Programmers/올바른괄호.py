def solution(s):
    if s.count('(') != s.count(')'):
        return False
    a = 0 
    for i in s:
        if i == '(':
            a += 1
        else :
            a -= 1
        if a<0:
            return False
    return True
  