import re

def solution(files):
    answer = []
    
    for i in range(len(files)):
        files[i] = re.split('([0-9]+)',files[i])
    files = sorted(files,key=lambda x:(x[0].lower(),int(x[1])))

    for file in files:
        answer.append(''.join(map(str,file)))
        
    return answer
    

