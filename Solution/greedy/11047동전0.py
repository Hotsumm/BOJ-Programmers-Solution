n,k = map(int,input().split())
coin = list()
for _ in range(n):
    coin.append(int(input()))
coin.reverse()

sum = 0
for i in range(n):
    sum += k//coin[i]
    k = k%coin[i]
print(sum)
    