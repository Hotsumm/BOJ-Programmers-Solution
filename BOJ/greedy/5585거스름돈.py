n = int(input())
change = 1000-n
coin = [500,100,50,10,5,1]
sum = 0
for i in coin:
    sum += change//i
    change = change%i
print(sum)

"""
p = int(input())
m = 1000-p
print(m//500+(m%500)//100+(m%100)//50+(m%50)//10+(m%10)//5+(m%5)//1)
"""