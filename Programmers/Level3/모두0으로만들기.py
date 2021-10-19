import sys
sys.setrecursionlimit(300000)

def dfs(i,a,tree,answer):
    global visited
    
    visited[i] = 1
    v = a[i]
    for t in tree[i]:
        if not visited[t]:
            v += dfs(t,a,tree,answer)
    answer.append(abs(v))
    return v

def solution(a, edges):
    global visited
    answer = []
    tree = [[] for _ in range(len(a))]

    if sum(a) != 0:
        return -1
    
    for edge in edges:
        e1,e2 = edge
        tree[e1].append(e2)
        tree[e2].append(e1)

    visited = [0]*len(a)
    dfs(0,a,tree,answer)

    return sum(answer)
