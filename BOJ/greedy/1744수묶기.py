n = int(input())

plus,minus = list(),list()
zero = 0
for _ in range(n):
    num = int(input())
    if num >0:
        plus.append(num)
    elif num==0:
        zero += 1
    else:
        minus.append(num)
sum = 0

plus.sort()
minus.sort(reverse=True)

if len(plus)%2==0 :
    while len(plus)>0 and plus[0] == 1:
        sum += plus[0] + plus[1]
        del plus[:2]
    if len(plus)%2!=0:
        sum += plus[0]
    for i in range(len(plus)//2):
        sum += plus[2*i] * plus[(2*i)+1]
else:
    if len(plus) == 1:
        sum = plus[0]
    else:
        sum += plus[0]
        del plus[0]
        while len(plus)>0 and plus[0] == 1:
            sum += plus[0] + plus[1]
            del plus[:2]
        for i in range(len(plus)//2):
            sum += plus[2*i] * plus[(2*i)+1]
            
if len(minus) % 2 ==0:
    for i in range(len(minus)//2):
        sum += minus[2*i] * minus[(2*i)+1]
else :
    if zero == 0:
        sum += minus[0]
        del minus[0]
        for i in range(len(minus)//2):
            sum += minus[2*i] * minus[(2*i)+1]
    else :
        if len(minus) != 1:
            del minus[0]
            for i in range(len(minus)//2):
                sum += minus[2*i]*minus[(2*i)+1]
print(sum)
    
