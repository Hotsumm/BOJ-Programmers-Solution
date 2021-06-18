def solution(dirs):
    answer = 0
    visited = []
    x, y = 5, 5
    
    for d in dirs:
        if d == 'U':
            if 0<=x-1<=10:
                temp = [x,y,x-1,y]
                x-= 1
            else: continue
        elif d == 'D':
            if 0<=x+1<=10:
                temp = [x,y,x+1,y]
                x += 1
            else: continue
        elif d == 'L':
            if 0<=y-1<=10:
                temp = [x,y,x,y-1]
                y -= 1
            else: continue
        elif d == 'R':
            if 0<=y+1<=10:
                temp = [x,y,x,y+1]
                y+= 1
            else: continue
            
        a1,b1,a2,b2 = temp
        if temp not in visited and [a2,b2,a1,b1] not in visited: 
            answer += 1
            visited.append(temp)
            visited.append([a2,b2,a1,b1])
        

    return answer


