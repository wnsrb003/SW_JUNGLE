import sys
sys.stdin = open('input.txt')
from collections import deque, defaultdict

N, M = map(int, sys.stdin.readline().strip().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().strip().split())
    graph[x][y] = 1
    graph[y][x] = 1


# def bfs(graph, start, visited):
#     visited[start] = 1
#     q = deque()
#     q.append(start)
#     while q:
#         x = q.pop()
#         for i in graph[x]:
            # if not visited[i]:

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j :
                continue
            elif graph[i][k] and graph[k][j]:
                if graph[i][j] == 0:
                    graph[i][j] = graph[i][k] + graph[k][j]
                else:
                    graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])
# for g in graph:
#     print(g)

최소 = 100000000
for i in range(1, N+1):
    temp = 0
    for j in range(1, N+1):
        temp += graph[i][j]
    if 최소 > temp:
        최소 = temp
        인싸 = i
print(인싸)