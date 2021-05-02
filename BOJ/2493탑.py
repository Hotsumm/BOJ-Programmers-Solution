import sys

n = int(sys.stdin.readline())
tower = list(map(int,sys.stdin.readline().rstrip().split()))
stack = []
answer = []

for t in range(len(tower)):
    while stack:
        if stack[-1][1] < tower[t]:
            stack.pop()
        else:
            answer.append(stack[-1][0]+1)
            stack.append([t,tower[t]])
            break
    if not stack:
        answer.append(0)
    stack.append([t,tower[t]])
print(" ".join(map(str,answer)))
