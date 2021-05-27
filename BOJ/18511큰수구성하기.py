import sys
input = sys.stdin.readline
from itertools import product

n, k = map(int,input().split())
number = list(map(int,input().split()))
answer = []
p = []
for i in range(1,len(str(n))+1):
    p.extend(list(product(number,repeat=i)))

for i in range(len(p)):
    p[i] = ''.join(map(str,p[i]))
    if int(p[i]) <= n:
        answer.append(int(p[i]))

print(max(answer))

