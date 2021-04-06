num_list = list()

for i in range(9):
    num_list.append(int(input()))
print(max(num_list))
print(int(num_list.index(max(num_list))+1))