import sys
input = sys.stdin.readline
from itertools import permutations

n, k = int(input()),int(input())
card = [int(input()) for _ in range(n)]
p = list(permutations(card,k))

for i in range(len(p)):
    p[i] = ''.join(map(str,p[i]))
p = list(set(p))
print(len(p))
    
