
def bfs(m,n,board):
    cnt = 0
    while True:
        locations = []
        arr = []
        for i in range(n-1):
            for j in range(m-1):
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] != -1:
                    locations.append([i,j])
                    locations.append([i+1,j])
                    locations.append([i,j+1])
                    locations.append([i+1,j+1])
        if locations:
            locations = [location for location in locations if location not in arr and not arr.append(location)]
            cnt  += len(locations)
            for x,y in locations:
                board[x][y] = 0
            for i,b in enumerate(board):
                empty = [-1] * b.count(0)
                board[i] = empty + [item for item in board[i] if item != 0 ]
        else :
            return cnt
        
def solution(m, n, board):
    answer = 0
    board = list(map(list,zip(*board)))
    answer = bfs(m,n,board)
    return answer
print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))

