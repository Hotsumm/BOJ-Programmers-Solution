from itertools import permutations

def solution(k, dungeons):
    answer = 0

    for dungeon_pm in permutations(dungeons):
        cnt = 0
        curr = k
        for dungeon in dungeon_pm:
            if curr < dungeon[0]:
                break
            curr -= dungeon[1]   
            if curr < 0:
                break
            cnt += 1
            
        answer = max(answer,cnt)
        
    return answer
