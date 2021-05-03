import sys
n = int(sys.stdin.readline())
book = dict()

for i in range(n):
    name = sys.stdin.readline().rstrip()
    if name in book:
        book[name] += 1
    else:
        book[name] = 1

answer = [k for k,v in book.items() if max(book.values()) == v]
answer.sort()
print(answer[0])
    
