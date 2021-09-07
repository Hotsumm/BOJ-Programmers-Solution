import sys
from collections import deque
input = sys.stdin.readline

left = deque(input().rstrip())
right = deque()
n = int(input())

for _ in range(n):
    cmd = list(input().split()) 
    if cmd[0] == 'B':
        if not left:
            continue
        left.pop()
    elif cmd[0] == 'P':
        left.append(cmd[1])
    else :
        if cmd[0] == 'L':
            if not left:
                continue
            right.appendleft(left.pop())
        if cmd[0] == 'D':
            if not right:
                continue
            left.append(right.popleft())
            

print(''.join(map(str,left+right)))
            
    

