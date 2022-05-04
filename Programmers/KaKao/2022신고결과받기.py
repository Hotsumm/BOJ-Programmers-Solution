def solution(id_list, report, k):
    answer = []
    temp = {}
    _dict = {}
    report = list(set(report))
    
    for _id in id_list:
        temp[_id] = 0
        _dict[_id] = [0,[]]

    for r in report:
        r1,r2 = r.split()
        if r1 not in _dict[r2][1]:
            _dict[r2][1].append(r1)
            _dict[r2][0] += 1

    for key,value in _dict.items():
        if value[0] >= k :
            while value[1]:
                temp[value[1].pop()] += 1

    answer = list(temp.values()) 
    return answer