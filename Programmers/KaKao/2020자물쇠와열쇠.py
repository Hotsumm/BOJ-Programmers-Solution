import copy

def rotate90(i,j,key,new_lock,open_lock,n,m):
    test_lock = copy.deepcopy(new_lock)
    check,temp = [],[]
    for each in zip(*key):              #시계방향 90도 회전
        temp.append(list(reversed(each)))

    for a in range(len(temp)):
        for b in range(len(temp[0])):
            if temp[a][b] == 1:
                test_lock[i+a][j+b] += 1        
    
    for c in range(m):
        check.append(test_lock[n-1+c][n-1:n+m-1])

    if check == open_lock:
        return (temp,True)
    else:
        return (temp,False)


def solution(key, lock):
    answer = False
    n,m = len(key),len(lock)
    new_lock = [[0]*((2*n)+(m-2)) for _ in range((2*n)+(m-2))]
    open_lock = [[1]*m for _ in range(m)]
    
    for i in range(m):
        for j in range(m):
            if lock[i][j] == 1:
                new_lock[i+n-1][j+n-1] = 1



    for i in range(n+m-1):
        for j in range(n+m-1):
            for k in range(4):
                key,result = rotate90(i,j,key,new_lock,open_lock,n,m)
                if result:
                    return True
 
    return answer

