import sys
input = sys.stdin.readline

n = int(input())
friends = [[0]*n for _ in range(n)]
people = [list(input().strip()) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if j==k:
                continue
            elif people[j][k] == 'Y' or (people[j][i] == 'Y' and people[k][i] =='Y'):
                friends[j][k] = 1
                
for friend in friends:
    answer= max(answer,sum(friend))
                
print(answer)
            
      

