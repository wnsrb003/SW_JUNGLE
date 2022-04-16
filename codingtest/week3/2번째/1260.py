# DFS
import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')
N, M, V = map(int, sys.stdin.readline().split())
stack = []
graph = defaultdict(list)
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    graph[i].sort()

def dfs(graph, v, visited):
    print(v, end=' ')
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        visited[v] = True
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * (N+1)
dfs(graph, V, visited)
print()
visited = [False] * (N+1)
bfs(graph, V, visited)