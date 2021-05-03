import sys

s = list(sys.stdin.readline().rstrip())
stack =[]
k = 0
for i in s:
    if i == ')':
        k = 0
        while stack:
            temp = stack.pop()
            if temp == '(':
                if k == 0:
                    stack.append(2)
                else:
                    stack.append(k*2)
                break
            elif temp == '[':
                print(0)
                exit(0)
            else:
                k += temp 
    elif i == ']':
        k = 0
        while stack:
            temp = stack.pop()
            if temp == '[':
                if k == 0:
                    stack.append(3)
                else:
                    stack.append(k*3)
                break
            elif temp == '(':
                print(0)
                exit(0)
            else:
                k += temp
    else:
        stack.append(i)
sum = 0
for item in stack:
    if type(item) != int :
        print(0)
        exit(0)
    else :
        sum += item
print(sum)

