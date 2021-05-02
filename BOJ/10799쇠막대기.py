import sys
stack = list(sys.stdin.readline())
left = 0
cnt = 0

while stack:
    temp = stack.pop(0)
    if temp =='(':
        if stack[0] == ')':
            stack.pop(0)
            cnt += left 
            continue
        left +=1
        cnt += 1 
    elif temp == ')':
        left -=1
print(cnt)
