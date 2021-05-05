import sys
n = int(sys.stdin.readline())
answer = 0
for _ in range(n):
    word = list(sys.stdin.readline().rstrip())
    stack = []
    while word:
        temp = word.pop()
        if not stack or stack[-1] != temp:
            stack.append(temp)
        elif stack[-1] == temp:
            stack.pop()
    if not stack:
        answer +=1 
           
print(answer)

