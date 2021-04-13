def dfs(computers,visited,i,n):
    visited[i] = 1
    for j in range(n):
        if visited[j] == 0 and computers[i][j] == 1:
            dfs(computers,visited,j,n)
    

def solution(n, computers):
    answer = 0
    visited = [0]*n
    for i in range(n):
        if visited[i] == 0:
            dfs(computers,visited,i,n)
            answer += 1
                
    return answer