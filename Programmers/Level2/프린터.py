from collections import deque

def solution(priorities, location):
    answer = 0
    deq = deque([(i,idx) for idx, i in enumerate(priorities)])
    target = deq[location][1]

    while True:
        a = deq.popleft()
        if deq and max(deq)[0] > a[0]:
            deq.append(a)
            continue
        if target == a[1]:
            answer += 1
            return answer
        answer += 1


