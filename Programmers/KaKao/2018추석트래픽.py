def calc(start,time_list):
    cnt = 0
    end = start + 999
    for s,e in time_list:
        if start<=e and end>=s:
            cnt += 1
    return cnt

def solution(lines):
    answer = 0
    time_list = []
    for line in lines:
        line = line.split()
        ho,mi,se = line[1].split(':')
        ms = int(ho)*60*60*1000 + int(mi)*60*1000 + float(se)*1000
        process_ms = float(line[2][:-1]) * 1000
        time_list.append([ms-process_ms+1,ms])
    for time in time_list:
        start,end = time
        answer = max(calc(start,time_list),answer)
        answer = max(calc(end,time_list),answer)
                         
    return answer


