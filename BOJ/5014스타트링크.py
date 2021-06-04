from collections import deque
import sys
input = sys.stdin.readline

def elevator():
    cnt = 0
    while move:
        for _ in range(len(move)):
            a = move.popleft()
            if a == g:
                return cnt
            for m in up_down:
                temp = a+m
                if 0<temp<f+1 and not visited[temp] :
                    move.append(temp)
                    visited[temp] = 1
        cnt += 1
    return 'use the stairs'

f,s,g,u,d = map(int,input().split())
up_down = [u,-d]
visited = [0]*(f+1)
visited[s] = 1
move = deque()
move.append(s)

print(elevator())
