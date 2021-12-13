import sys
import heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    answer = 0
    files = list(map(int,input().split()))
    heapq.heapify(files)
    while len(files) != 1:
        a,b = heapq.heappop(files),heapq.heappop(files)
        sum_file = a + b
        answer += sum_file
        heapq.heappush(files,sum_file)
    print(answer)
        