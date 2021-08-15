import sys
input = sys.stdin.readline

n,m = map(int,input().split())

p = [int(input()) for _ in range(n)]
p.sort()

answer = 2000000001

left = 0
right = 0

while left < n and right < n:
    calc = p[right] - p[left]
    if calc > m:
        if answer > calc:
            answer = calc
        left += 1
    elif calc < m :
        right += 1
    else:
        answer  = calc
        break
    
print(answer)
        
