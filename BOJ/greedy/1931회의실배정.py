n = int(input())
table = list()

for i in range(n):
    table.append(list(map(int,input().split())))
table.sort(key = lambda x:(x[1],x[0]))

end_time =0 
cnt = 0
for i in range(n):
    if end_time<=table[i][0]:
        cnt +=1
        end_time = table[i][1]

print(cnt)