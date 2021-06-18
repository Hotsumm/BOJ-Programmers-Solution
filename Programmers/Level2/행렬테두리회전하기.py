def rotate(query,board):
    x1,y1,x2,y2 = query
    first_num = board[x1-1][y1-1]
    min_num = first_num
    
    for i in range(x1-1,x2-1): #왼쪽세로
        temp = board[i+1][y1-1]
        board[i][y1-1] = temp
        min_num = min(min_num,temp) 

    for i in range(y1-1,y2-1): #아래세로
        temp = board[x2-1][i+1]
        board[x2-1][i] = temp
        min_num = min(min_num,temp)
    
    for i in range(x2-1,x1-1,-1): #오른쪽세로
        temp = board[i-1][y2-1]
        board[i][y2-1] = temp
        min_num = min(min_num,temp)
        
    for i in range(y2-1,y1-1,-1): # 위가로
        temp = board[x1-1][i-1]
        board[x1-1][i] = temp
        min_num = min(min_num,temp)
    board[x1-1][y1] = first_num

    return min_num
    
def solution(rows, columns, queries):
    answer = []
    board = [[] for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            board[i].append(j+1+(i*columns))
            
    for query in queries:
        answer.append(rotate(query,board))

    
    return answer


