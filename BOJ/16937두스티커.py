import sys
input = sys.stdin.readline

h,w = map(int,input().split())
n = int(input())
stickers = [list(map(int,input().split())) for _ in range(n)]
answer = []
while len(stickers) != 1:
    a,b = stickers.pop()
    for sticker in stickers:
        c,d = sticker
        if a+c<=h and max(b,d)<=w:
            answer.append(a*b + c*d)
        elif a+c<=w and max(b,d)<=h:
            answer.append(a*b + c*d)
        elif b+d<= w and max(a,c) <= h:
            answer.append(a*b + c*d)
        elif b+d <= h and max(a,c) <= w:
            answer.append(a*b + c*d)
        elif a+d<=w and max(b,c) <= h:
            answer.append(a*b + c*d)
        elif a+d<=h and max(b,c) <= w:
            answer.append(a*b + c*d)
        elif b+c<=h and max(a,d) <=w:
            answer.append(a*b + c*d)
        elif b+c<=w and max(a,d) <=h:
            answer.append(a*b + c*d)
       
if answer:
    print(max(answer))
else:
    print(0)


