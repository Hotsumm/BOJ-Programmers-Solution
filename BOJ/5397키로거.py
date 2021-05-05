from collections import deque
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    left,right = deque(),deque()
    l = list(sys.stdin.readline().rstrip())
    for p in l:
        if p == '<':
            if left:
                right.appendleft(left.pop())
        elif p == '>':
            if right:
                left.append(right.popleft())
        elif p == '-':
            if left:
                left.pop()
        else:
            left.append(p)
    left.extend(right)
            
        
    print(''.join(left))
        
        
        
