def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x:x[2])
    connect = set([costs[0][0]])
    
    for cost in costs:
        a,b,c = cost
        if a in connect and b in connect:
            continue
        elif a in connect or b in connect:
            connect.update([a,b])
            answer += c
    
    
    return answer
    

"""
## 크루스칼 알고리즘(Kruskal Algorithm)

def find(parent,x):
    if parent[x] == x:
        return x
    parent[x] = find(parent,parent[x])
    return parent[x]
        

def union(parent,a,b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
  
def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x:x[2])
    parent = [0]*n
    
    for i in range(n):
        parent[i] = i
    
    for cost in costs:
        a,b,c = cost
        if find(parent,a) != find(parent,b):
            union(parent,find(parent,a),find(parent,b))
            answer += c
    
    return answer
"""     
