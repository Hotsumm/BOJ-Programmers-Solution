n= int(input())
score_list = list(map(int,input().split()))
score_sum = 0

for i in range(n):
    score_sum += (score_list[i]/max(score_list)) * 100 
print(score_sum/n)