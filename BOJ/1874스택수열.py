import sys

n = int(sys.stdin.readline())
stack = []
answer= []
curr = 0
check = True
for _ in range(n):
    x = int(sys.stdin.readline())
    while curr<x:
        curr +=1
        stack.append(curr)
        answer.append('+')
    if stack and stack[-1] == x:
        stack.pop()
        answer.append('-')
    else:
        check = False
        break
if check :
    for k in answer:
        print(k)
else:
    print('NO')
            
