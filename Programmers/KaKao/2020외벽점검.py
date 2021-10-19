from itertools import permutations


# 완전탐색 어떤친구가 어디서부터 점검을 시작할건지

def solution(n, weak, dist):
    answer = 0
    _min = []

    w_n = len(weak)
    weak_ln = weak + [n+w for w in weak]  #취약지점을 선형으로

    
    for i,start in enumerate(weak):      # 취약지점의 시작위치
        for friends in permutations(dist):  
            cnt = 1             # 처음은 1명으로 시작
            curr = start        # 처음 친구가 점검할 최초위치
            for f in friends:
                curr += f           # 처음은 1명으로 시작
                if curr < weak_ln[w_n+i-1]:     # 이동한 거리가 취약지점 거리보다 작다면 => 친구 1명추가
                    for temp in weak_ln[i+cnt:]:
                        if curr < temp:
                            curr = temp
                            cnt +=1             #친구 한명추가
                            break
                else:           # 이동한 거리가 취약지점 거리와 같거나 크다면 => 모두 점검완료
                    _min.append(cnt)
                    break
    
    answer = -1 if not _min else min(_min)   
    
    return answer

