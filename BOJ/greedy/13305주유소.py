n = int(input())
length = list(map(int,input().split()))
price = list(map(int,input().split()))

sum_price = 0
idx =0
if min(price)==price[0]:
    sum_price = price[0]*sum(length)
else:
    for i in range(n-1):
        sum_price += price[idx]*length[i]
        if price[idx]>price[i+1]:
            idx=i+1
print(sum_price)