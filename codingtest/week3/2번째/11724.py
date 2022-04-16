import sys
from collections import defaultdict,deque
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
# graph = defaultdict(list)
graph = []
for i in range(M):
    x, y  = map(int, sys.stdin.readline().split())
    graph.append([x,y])
    # graph[y].append(x)
for i in graph:
    i.sort()
visited = [False] * (N+1)
cnt = 0
# def dfs(graph, v, visited):
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         a = queue.popleft()
#         for i in graph[a]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
# for i in range(1, N+1):
#     if not visited[i]:
#         bfs(graph, i, visited)
#         cnt += 1

union = [i for i in range(N+1)]
def find(x):
    if x != union[x]:
        union[x] = find(union[x])
    return union[x]
for i in graph:
    x = find(i[0])
    y = find(i[1])
    if x != y :
        if x < y:
            union[y] = x
        else :
            union[x] = y
for i in range(1, N+1):
    while union[i] != union[union[i]]:
        union[i] = union[union[i]]
print(len(set(union)) - 1)