while True:
    cnt = 0
    dx = [1,-1,0,0,1,-1,1,-1]
    dy = [0,0,1,-1,1,-1,-1,1]
    w, h = map(int,input().split())
    if w==0 and h==0:
        break
    
    def bfs(i,j):
        queue = [[i,j]]
        while queue:
            b, a = queue[0][0],queue[0][1]
            del queue[0]
            for k in range(8):
                x = dx[k] + a
                y = dy[k] + b
                if 0<=x<w and 0<=y<h and square[y][x] == 1:
                    square[y][x] = 0
                    queue.append([y,x])
                    
    square = []
    for _ in range(h):
        square.append(list(map(int,input().split())))
    for i in range(h):
        for j in range(w):
            if square[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)
