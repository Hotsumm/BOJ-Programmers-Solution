import sys
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    rank = list()
    for _ in range(n):
        rank.append(list(map(int,sys.stdin.readline().split())))
    rank.sort(key=lambda x:x[0])
    cnt = 1
    max_rank = rank[0][1]
    for i in range(1,n):
        if max_rank > rank[i][1]:
            cnt +=1
            max_rank = rank[i][1]
    print(cnt)