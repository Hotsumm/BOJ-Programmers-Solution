import sys

input = sys.stdin.readline
n, m = map(int,input().split())
dnas = [input().strip() for _ in range(n)]
d = ['A','C','G','T']
answer = ''
cnt = 0
for i in range(m):
    temp = [0]*4
    for dna in dnas:
        for j in range(4):
            if dna[i]==d[j]:
                temp[j] += 1
    cnt += n - max(temp)
    answer += d[temp.index(max(temp))]
print(answer)
print(cnt)
     