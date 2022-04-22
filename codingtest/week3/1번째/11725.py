import sys
from collections import defaultdict
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
graph = defaultdict(list)
try:
    while(True):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
except:
    pass
print(graph)
visited = [False] * (N+1)
result = [0] * (N+1)
def dfs(graph, index, visited):
    visited[index] = True
    for i in graph[index]:
        if not visited[i]:
            dfs(graph, i, visited)
            result[i] = index
dfs(graph, 1, visited)
print('\n'.join(list(map(str, result[2:]))))