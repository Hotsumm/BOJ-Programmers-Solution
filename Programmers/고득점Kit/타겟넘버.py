from itertools import combinations

def solution(numbers, target):
    answer = 0
    if sum(numbers) == target:
        return 1

    for i in range(1,len(numbers)):
        combi = list(combinations(numbers,i))
        for j in range(len(combi)):
            if target == sum(numbers) - sum(combi[j])*2:
                answer += 1 
    return answer