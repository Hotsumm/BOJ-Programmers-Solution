#sys.stdin.readline()
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int,sys.stdin.readline().split())
    first = list(map(int,sys.stdin.readline().rstrip().split()))
    seq = []
    for i,item in enumerate(first):
        seq.append([item,i])
    cnt = 0
    target = seq[m][0]
    target_idx = m
    first.sort()
    while True:
        curr = seq.pop(0)
        num = curr[0]
        idx = curr[1]
        if num == first[-1]:
            cnt += 1
            first.pop()
            if num == target and idx == target_idx:
                print(cnt)
                break
        else:
            seq.append([num,idx])
