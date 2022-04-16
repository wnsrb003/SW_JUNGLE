import sys
from collections import deque, defaultdict

sys.stdin = open('input.txt')

N, M, V = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
for i in graph.keys():
    graph[i].sort()

def dfs(graph, x, visited):
    visited[x] = True 
    print(x, end=' ')
    for i in graph[x]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        pop = queue.popleft()
        print(pop, end=' ')
        for i in graph[pop]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
visited = [False] * (N+1)
dfs(graph, V, visited)
print()
visited = [False] * (N+1)
bfs(graph, V, visited)

