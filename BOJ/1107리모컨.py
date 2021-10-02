""" 반례가 없는데 틀림
from itertools import product
import heapq
import sys
input = sys.stdin.readline

def push():
    if n == 100:
        return 
    heapq.heappush(answer,abs(100 - n))
    for pr in product(btn,repeat=len(str(n))):
        pr = list(pr)
        temp = ''
        while pr:
            temp += str(pr.pop())
        temp = int(temp)
        heapq.heappush(answer,abs(temp - n)+len(str(n)))
     
    if len(str(n)) > 1:
        for pr in product(btn,repeat=len(str(n))-1):
            pr = list(pr)
            temp = ''
            while pr:
                temp += str(pr.pop())
            temp = int(temp)
            heapq.heappush(answer,abs(temp - n)+len(str(n))-1)


n = int(input())
m = int(input())
p = list(map(int,input().split()))

btn = [i for i in range(10) if i not in p]
answer = []


push()

if not answer:
    print(0)
else:
    print(heapq.heappop(answer))
"""
    
n = int(input())
m = int(input())
ms = []
if m != 0:
    ms = list(input().split())

ans = 999999999
length = 0
for i in range(1000000):
    broken = False
    for s in str(i):
        if s in ms:
            broken = True
    if broken:
        pass
    else:
        if ans > abs(n - i):
            ans = abs(n - i)
            length = len(str(i))

ans = min(ans + length, abs(n - 100))

print(ans)