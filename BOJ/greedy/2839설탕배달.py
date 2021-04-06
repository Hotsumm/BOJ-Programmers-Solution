n = int(input())

if n%5 == 0:
    print(n//5)
else:
    for i in range(1,(n//3)+1):
        if (n-3*i)%5 ==0:
            print(i+(n-3*i)//5)
            break
        if i == n//3:
            print(-1)

"""
n = int(input())
cnt = 0

while n>=0:
    if n%5==0:
        print(cnt+(n//5))
        break
    else:
        cnt += 1
        n -=3
else:
    print(-1)
"""