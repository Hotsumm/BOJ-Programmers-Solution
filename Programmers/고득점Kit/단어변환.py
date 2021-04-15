def dfs(begin,target, words,visited):
    stacks = [begin]
    cnt = 0
    while stacks:
        for _ in range(len(stacks)):
            stack = stacks.pop()
            if stack == target:
                if len(stacks)==0:
                    return cnt
                return cnt+1
            for i in range(len(words)):
                if len([j for j in range(len(words[i])) if stack[j] != words[i][j]]) == 1:
                    if visited[i] == 0:
                        visited[i] = 1
                        stacks.append(words[i])
        cnt += 1
    return cnt 

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    visited = [0] * len(words)
    answer = dfs(begin,target,words,visited)
        
    return answer


