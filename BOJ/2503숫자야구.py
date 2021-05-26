import sys
from itertools import permutations
input = sys.stdin.readline
t = int(input())
answer = list(permutations([1,2,3,4,5,6,7,8,9],3))

for _ in range(t):
    q,s,b = map(int,input().split())
    q = list(str(q))
    remove_cnt = 0
    for i in range(len(answer)):
        s_n,b_n = 0,0
        i -= remove_cnt
        for j in range(3):
            q[j] = int(q[j])
            if q[j] in answer[i]:
                if j == answer[i].index(q[j]):
                    s_n += 1
                else:
                    b_n += 1
        if s != s_n or b != b_n:
            remove_cnt += 1
            answer.remove(answer[i])
print(len(answer))
