def build(board):
    n = len(board)
    stack = []
    stack.append([0,0,'first'])
    board[0][0] = -500
    while stack:
        a,b,d = stack.pop()
        for dx, dy, drt in ((-1, 0, 'U'), (0, -1, 'L'), (1, 0, 'D'), (0, 1, 'R',)):
            x = a + dx
            y = b + dy
            if 0<=x<n and 0<=y<n and board[x][y] != 1 :
                cost = board[a][b] + 100
                if d != drt:
                    cost += 500
                if cost <= board[x][y] or board[x][y] == 0:
                    stack.append([x,y,drt])
                    board[x][y] = cost
                    
    return board[-1][-1] 
                    
def solution(board):
    answer = 0    
    answer = build(board)
    return answer


