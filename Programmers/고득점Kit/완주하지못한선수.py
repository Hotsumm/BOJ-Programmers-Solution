def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for a,b in zip(participant,completion):
        if a!=b:
            answer = a
            return answer
    answer = participant[-1]
    return answer

