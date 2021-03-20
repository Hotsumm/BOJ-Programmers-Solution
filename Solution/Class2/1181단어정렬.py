t = int(input())
word_list = list()

for _ in range(t):
    word_list.append(input())
word_list = list(set(word_list))    
word_list.sort()
word_list.sort(key=len)
for i in range(len(word_list)):
    print(word_list[i])
