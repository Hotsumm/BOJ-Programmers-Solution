import sys
n = int(sys.stdin.readline())
name = dict()

for i in range(n):
    temp = sys.stdin.readline().rstrip()
    if temp in name:
        name[temp] += 1
    else:
        name[temp] = 1
        
for i in range(n-1):
    temp = sys.stdin.readline().rstrip()
    name[temp] -= 1
    
for s in name:
    if name[s] != 0:
        print(s)


    
