import sys
input = sys.stdin.readline


n = int(input())
a,b,c,d = [],[],[],[]

a_b = {}
cnt = 0

for _ in range(n):
    a_n,b_n,c_n,d_n = list(map(int,input().split()))  
    a.append(a_n)
    b.append(b_n)
    c.append(c_n)
    d.append(d_n)

for _a in a:
    for _b in b :
        if not a_b.get(_a+_b):
            a_b[_a + _b] = 1
        else:
            a_b[_a + _b] += 1


for _c in c:
    for _d in d:
        v =  _c+_d
        if -v in a_b.keys():
            cnt += a_b[-v]
print(cnt)
