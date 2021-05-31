import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)
t = int(input())

def dfs(i):
    visited[i] = 1
    record.append(i)
    v = s[i]
    if visited[v] == 0:
        dfs(v)
    else:
        if v in record:
            for num in record[record.index(v):]:
                answer.append(num)
        return 
        
        
for _ in range(t):
    answer = []
    n = int(input())
    s = [0] + list(map(int,input().split()))
    visited = [0]*(n+1)
    for i in range(1,n+1):
        if visited[i] == 0 :
            record = []
            dfs(i)
    print(n-len(answer))
