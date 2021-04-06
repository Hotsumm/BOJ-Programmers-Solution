n = int(input())

for i in range(n):
    score = 0
    count = 1
    result = input()
    for j in range(len(result)):
        if result[j] == 'O':
            score += count
            count += 1
        elif result[j] == 'X':
            count = 1
    print(score)