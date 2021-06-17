def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        temp=''
        for word in skill_trees[i]:
            if word in skill:
                temp += word
        skill_trees[i] = temp

    for skill_tree in skill_trees:
        if not skill_tree:
            answer+=1
            continue
        for i in range(1,len(skill)+1):
            if skill_tree == skill[:i]:
                answer += 1
                break
    return answer
