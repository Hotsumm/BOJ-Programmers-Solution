import sys
import heapq
input = sys.stdin.readline

n = int(input())
p = input().strip()
b,r = 0,0
if p[0] == 'B':
    b += 1
else:
    r += 1
curr = p[0]

for item in p[1:]:
    if item == 'B':
        if curr == 'B':
            continue
        curr = 'B'
        b += 1
    if item == 'R':
        if curr == 'R':
            continue
        curr = 'R'
        r += 1
if b>r:
    print(1+r)
elif b<r:
    print(1+b)
else:
    print(1+b)

    
    


