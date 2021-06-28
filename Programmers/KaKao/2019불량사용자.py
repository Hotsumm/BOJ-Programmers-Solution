from itertools import permutations

def solution(user_id, banned_id):
    answer = []
    n = len(banned_id)
    user_id = list(permutations(user_id,n))
    
    for p in user_id:
        check = True
        for u_id,b_id in zip(p,banned_id):
            if len(u_id) != len(b_id):
                check = False
                continue
            for u,b in zip(u_id,b_id):
                if b == '*':
                    continue
                else:
                    if u != b:
                        check = False            
                        break
            if not check:
                break
        if check :
            answer.append(p)
            
    for i in range(len(answer)):
        answer[i] = sorted(answer[i])
    answer = list(set([tuple(set(item)) for item in answer]))
        
    
    return len(answer)

