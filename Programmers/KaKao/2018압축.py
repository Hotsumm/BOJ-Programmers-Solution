def solution(msg):
    answer = []
    d = {}
    num = 27
    idx = 0
    last_idx = 0
    for i in range(65,91):
        d[chr(i)] = i-64
    while idx<len(msg):
        w = ''
        for i in range(idx+1,len(msg)+1):
            if msg[idx:i] in d :
                w = msg[idx:i]
                last_idx = i
        idx = last_idx
        answer.append(d.get(w))
        if idx<len(msg):
            d[w+msg[idx]] = num
            num += 1

    return answer

