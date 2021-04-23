def solution(str1, str2):
    str1,str2= str1.upper(),str2.upper() 
    answer = 0
    str1 = [str1[i]+str1[i+1] for i in range(len(str1)-1) if (str1[i]+str1[i+1]).isalpha()]
    str2 = [str2[i]+str2[i+1] for i in range(len(str2)-1) if (str2[i]+str2[i+1]).isalpha()]
    intersection,union = 0,0
    for n in list(set(str1) & set(str2)):
        intersection += min(str1.count(n),str2.count(n))
    for m in list(set(str1) | set(str2)):
        union += max(str1.count(m),str2.count(m))
    if union == 0:
        return 65536
    jacquard = intersection/union
    answer = int(jacquard*65536)
    
    return answer

print(solution("a$%$#","efds=m*c^2"))




