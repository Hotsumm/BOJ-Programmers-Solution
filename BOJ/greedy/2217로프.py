n = int(input())
rope = list()
for i in range(n):
    rope.append(int(input()))
rope.sort()
weight = list()
for i in range(1,n+1):
    weight.append(rope[n-i]*i)
print(max(weight))
