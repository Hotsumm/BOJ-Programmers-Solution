import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int,input().split()))
p.sort()

c = 2000000001 
answer = []

left = 0
right = n-1

while left < right:
    calc = p[left] + p[right]
    if c > abs(calc):
        c = abs(calc)
        answer = [p[left]] + [p[right]]
    if calc < 0:
        left += 1
    elif calc > 0:
        right -= 1
    else:
        break
        
print(answer[0],answer[1])
    
    
    
