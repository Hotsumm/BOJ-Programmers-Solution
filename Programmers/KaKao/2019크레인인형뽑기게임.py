def solution(board, moves):
    answer = 0
    box = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                box.append(board[j][i-1])
                board[j][i-1] = 0
                if len(box)>1 and box[-1] == box[-2] :
                    answer += 2
                    box = box[:-2]
                break
    return answer