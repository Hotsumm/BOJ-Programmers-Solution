def solution(dartResult):
    answer = 0
    calc = []
    num = ''
    idx = -1
    for i in range(len(dartResult)):
        if dartResult[i].isnumeric():
            if i>0 and dartResult[i-1].isnumeric():
                num += dartResult[i]
            else :
                num = dartResult[i]
        elif dartResult[i] == 'S':
            calc.append(int(num)**1)
            num = ''
            idx += 1
        elif dartResult[i] == 'D':
            calc.append(int(num)**2)
            num = ''
            idx += 1
        elif dartResult[i] == 'T':
            calc.append(int(num)**3)
            num = ''
            idx += 1
        elif dartResult[i] == '*':
            calc[idx] *= 2
            if idx>0:
                calc[idx-1] *= 2
        elif dartResult[i] == '#':
            calc[idx] *= (-1)
    for i in calc:
        answer += i
    return answer