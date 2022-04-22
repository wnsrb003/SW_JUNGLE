import sys
sys.stdin = open('input.txt')
from collections import deque

nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]
N = int(sys.stdin.readline())

graph = []
for _ in range(N):
    graph.append(list(map(int, list(sys.stdin.readline().strip()))))

def bfs(graph, start, visited):
    i, j = start
    visited[i][j] = True
    q = deque()
    q.append((i,j))
    cnt = 1
    while q:
        x, y = q.pop()
        for n in range(4):
            dx = x + nx[n]
            dy = y + ny[n]
            if 0 <= dx < N and 0 <= dy < N and not visited[dx][dy] and graph[dx][dy] == 1:
                visited[dx][dy] = True
                cnt += 1
                q.append((dx,dy))
    return cnt

visited = [[False] * N for _ in range(N)]
result = 0 
count = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            result += 1
            count.append(bfs(graph, (i,j), visited))
print(result)
count.sort()
for c in count:
    print(c)