import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(sys.stdin.readline().strip()))))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, start, visited):
    global cnt
    x, y = start
    visited[x][y] = True
    q = deque()
    q.appendleft((x,y))
    while q:
        i, j = q.popleft()
        for n in range(4):
            nx = i + dx[n]
            ny = j + dy[n]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    cnt += 1
                    visited[nx][ny] = True
                    q.append((nx,ny))
result = []
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt = 1
            bfs(graph, (i,j), visited)
            result.append(cnt)
print(len(result))
result.sort()
print(*result)

# def dfs(graph, i, visited):
#     global cnt
#     x, y = i
#     visited[x][y] = True
#     for n in range(4):
#         nx = x + dx[n]
#         ny = y + dy[n]
#         if 0 <= nx < N and 0 <= ny < N:
#             if graph[nx][ny] == 1 and not visited[nx][ny]:
#                 cnt += 1
#                 dfs(graph, (nx, ny), visited)

# result = []
# visited = [[False] * N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         if graph[i][j] == 1 and not visited[i][j]:
#             cnt = 1
#             dfs(graph, (i,j), visited)
#             result.append(cnt)
# print(len(result))
# result.sort()
# print(*result)