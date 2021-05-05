while True:
    temp = []
    check = True
    p = input()
    if p == '.':
        break
    for i in p:
        if i == '(' or i == '[':
            temp.append(i)
        elif i == ')':
            if temp and temp[-1] == '(':
                temp.pop()
            else:
                check =False
                break
        elif i == ']':
            if temp and temp[-1] == '[':
                temp.pop()
            else :
                check =False
                break
    if not temp and check:
        print('yes')
    else:
        print('no')
            


