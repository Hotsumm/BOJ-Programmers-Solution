import sys
from collections import deque
input = sys.stdin.readline

def bfs(k):
    cnt = 0
    answer = 0
    while True:
        cnt += 1
        for _ in range(len(deq)):
            house = deq.popleft()
            for temp in [house+1,house-1]:
                if k == 0:
                    return answer
                if not visited.get(temp):
                    answer += cnt
                    visited[temp] = True
                    deq.append(temp)
                    k -= 1
        

n,k = map(int,input().split())
deq = deque(map(int,input().split()))
visited = {}
for num in deq:
    visited[num] = True
print(bfs(k))
