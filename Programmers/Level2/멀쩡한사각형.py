def solution(w,h):
    answer = 0
    g = 0
    if w==h:
        answer = w*h - h
    else:
        x,y = w,h
        if x>y:
            while y:
                x, y = y, x%y
            g = x
        elif y>x:
            while x:
                y, x = x, y%x
            g = y

        answer = w*h - (w+h-g)
    
        
    return answer



