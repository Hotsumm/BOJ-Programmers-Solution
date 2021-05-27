def solution(s):
    answer = 0
    arr = []

    for item in s:
        if arr and arr[-1] == item:
            arr.pop()
            continue
        arr.append(item)

    if not len(arr): answer = 1
    else : answer =0
    return answer

