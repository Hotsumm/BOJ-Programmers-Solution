n,k = map(int,input().split())
p = [i for i in range(1,n+1)]
answer = list()
idx = 0

while p:
    idx += k-1
    if idx>=len(p):
        idx = idx%len(p)
    answer.append(p.pop(idx))
print('<',end='')
print(', '.join(map(str,answer)),end='')
print('>')

    
