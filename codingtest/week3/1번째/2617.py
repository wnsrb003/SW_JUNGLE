import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**4)
from collections import defaultdict, deque
N, M = map(int, sys.stdin.readline().split())

heavy = defaultdict(list)
light = defaultdict(list)
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    heavy[x].append(y)
    heavy[y]
    light[y].append(x)
    light[x]

def dfs(graph, index, visited):
    global cnt
    visited[index] = True
    for i in graph[index]:
        if not visited[i]:
            cnt += 1
            dfs(graph, i, visited)
    return cnt

result = 0
for i in range(1, N+1):
    cnt = 0
    visited = [False for _ in range(N+1)]
    if dfs(heavy, i, visited) >= (N+1)//2:
        result += 1
    cnt = 0
    if dfs(light, i, visited) >= (N+1)//2:
        result += 1
print(result)