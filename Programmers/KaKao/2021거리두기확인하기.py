from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def check(p,place):
    for i,j in p:
        visited = [[0]*5 for _ in range(5)]
        visited[i][j] = 1
        deq = deque()
        deq.append([i,j,0])
        while deq:
            a,b,d = deq.popleft()
            if d > 1 :
                continue
            for k in range(4):
                x = dx[k] + a
                y = dy[k] + b
                if 0<=x<5 and 0<=y<5 and not visited[x][y] :
                    if place[x][y] == 'O':
                        deq.append([x,y,d+1])
                        visited[x][y] = 1
                    elif place[x][y] == 'P':
                        print(x,y)
                        return False
    return True

def solution(places):
    answer = []
    for place in places:
        p = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    p.append([i,j])
        if check(p,place):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer
