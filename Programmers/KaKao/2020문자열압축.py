def solution(s):
    answer = 0
    if len(s) == 1:
        answer = 1
        return answer
    cnt = 1
    compress = [''] * (len(s)//2)
    for i in range(1,len(s)//2+1):
        for j in range(0,len(s),i):
            if s[j:j+i] == s[j+i:j+(2*i)]:
                cnt += 1
            else :
                if cnt != 1:
                    compress[i-1] += str(cnt)+s[j:j+i]
                    cnt = 1
                else :
                    compress[i-1] +=  s[j:j+i]
                    cnt = 1
    answer = len(min(compress, key=len))
    return answer
