#Linked List

def solution(n, k, cmd):
    answer = ''
    stack = []
    nodes = {0: [n-1,1], n-1: [n-2,0]}

    for i in range(1,n-1):
        nodes[i] = [i-1,i+1]

    for c in cmd:
        c = c.split()
        cnt = 0
        if c[0] == 'C':
            nodes[nodes[k][0]][1] = nodes[k][1] 
            nodes[nodes[k][1]][0] = nodes[k][0]
            stack.append([k,nodes[k]])
            del_k = k
            if nodes[k][1] == 0 :
                k = nodes[k][0]
            else:
                k = nodes[k][1]
            del nodes[del_k]
            
        elif c[0] == 'Z':
            num, [prev, _next] = stack.pop()
            nodes[num] = [prev,_next]
            nodes[prev][1] = num
            nodes[_next][0] = num
        else :
            if c[0] == 'D':
                while cnt < int(c[1]):
                    k = nodes[k][1]
                    cnt += 1
                
            else:
                while cnt < int(c[1]):
                    k = nodes[k][0]
                    cnt += 1


    for i in range(n):
        if nodes.get(i) == None:
            answer += 'X'
        else :
            answer += 'O'
    return answer

