import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**6)

N, K = map(int, sys.stdin.readline().split())

def bfs():
    q = deque()
    q.append(N)
    visited[N] = 1
    while q:
        pop = q.popleft()
        if pop == K:
            print(visited[pop]-1)
            break
        for new in [pop*2, pop+1, pop-1]:
            if 0 <= new <= max and not visited[new]:
                visited[new] = visited[pop]+1
                q.append(new)
max = 2* 10 ** 5
visited = [0]*(max+1)
bfs()