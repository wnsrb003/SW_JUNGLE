import sys
from collections import defaultdict
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

def dfs(graph, index, visited, color):
    if color == 1:
        visited[index] = 2
    else :
        visited[index] = 1
    color = visited[index]
    for i in graph[index]:
        if not visited[i]:
            dfs(graph, i, visited, color)
            
for _ in range(N):
    V, E = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0] * (V+1)
    color = 1
    for i in range(1, len(visited)):
        if visited[i] == 0:
            dfs(graph, i, visited, color)

    result = 'YES'
    for i in graph.keys():
        for j in graph[i]:
            if visited[i] == visited[j]:
                result = 'NO'
                break
    print(result)