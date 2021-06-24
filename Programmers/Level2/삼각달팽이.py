def solution(n):
    answer = [[0 for i in range(j)] for j in range(1,n+1)]
    x,y = -1,0
    curr = 1
    for i in range(n):
        for j in range(i,n):
            if i%3 == 0:
                x += 1
            elif i%3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            answer[x][y] = curr
            curr += 1
        
    return sum(answer,[])
