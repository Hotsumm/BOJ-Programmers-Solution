import sys
input = sys.stdin.readline

n, k = map(int,input().split())
number = list(input().strip())
answer = []
for i in range(len(number)):
    while answer and k > 0 and answer[-1] < number[i]:
        answer.pop()
        k -= 1
    answer.append(number[i])
              
print(''.join(answer[:len(answer)-k]))
