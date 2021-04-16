def solution(progresses, speeds):
    answer = []
    day_list = []
    for idx,progress in enumerate(progresses):
        day = 0
        while progress < 100:
            progress += speeds[idx]
            day += 1
        day_list.append(day)

    curr = day_list.pop(0)
    cnt = 1 
    while day_list:
        if curr < day_list[0]:
            answer.append(cnt)
            curr = day_list.pop(0)
            cnt = 1
            continue
        day_list.pop(0)
        cnt += 1
    answer.append(cnt)
    return answer


