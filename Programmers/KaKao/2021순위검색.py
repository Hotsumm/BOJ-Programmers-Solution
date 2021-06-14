from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    d = {}
    for idx,item in enumerate(info):
        temp = item.split(' ')
        k = temp[:-1]
        score = int(temp[-1])
        for i in range(5):
            combi = list(combinations(k,i))
            for c in combi:
                case = ''.join(c)
                if case not in d.keys():
                    d[case] = [score]
                else:
                    d[case].append(score)
    for key in d.keys():
        d[key].sort()
    
    for i in query:
        i = i.replace(' and','')
        i = i.split(' ')
        condition = i[0]+i[1]+i[2]+i[3]
        condition = condition.replace('-','')
        score = int(i[4])
        cnt = 0
        if condition in d.keys():
            v = d[condition]
            cnt = len(v)- bisect_left(v,score,lo=0,hi=len(v))
        answer.append(cnt)        
    return answer
 

