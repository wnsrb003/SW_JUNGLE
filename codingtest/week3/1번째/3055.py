import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')

# 물 -> * , 돌 -> X, 비버굴 -> D, 고슴도치 -> S
dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

R, C = map(int, sys.stdin.readline().split())
graph = []
for _ in range(R):
    graph.append(list(sys.stdin.readline().strip()))

water = []
for i in range(R):
    for j in range(C):
        if graph[i][j] == '*':
            water.append((i,j))
        elif graph[i][j] == 'D':
            ending = (i,j)
        elif graph[i][j] == 'S':
            water.append((i,j))
cnt = 0           

def bfs(graph, start, visited):
    q = deque()
    for s in start:
        i, j = s
        if graph[i][j] == '*':
            q.append((i,j))
        elif graph[i][j] == 'S':
            q.appendleft((i,j))
    while q:
        x, y = q.popleft()
        for n in range(4):
            nx = x + dx[n]
            ny = y + dy[n]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[x][y] == '*':
                    if graph[nx][ny] == '.' or graph[nx][ny] == 'S':
                        graph[nx][ny] = '*'
                        q.append([nx,ny])
                elif graph[x][y] == 'S':
                    if graph[nx][ny] == '.':
                        visited[nx][ny] = visited[x][y] + 1
                        graph[nx][ny] = 'S'
                        q.append([nx,ny])
                    elif graph[nx][ny] == 'D':
                        visited[nx][ny] = visited[x][y] + 1
                        return visited[nx][ny]
    return 'KAKTUS'
visited = [[False] * C for _ in range(R)]
print(bfs(graph, water, visited))



# def dfs(graph, starting, visited):
    #     global cnt
#     x, y = starting
#     visited[x][y] = True
#     # if graph[x][y] == -1:
#     if x == ending[0] and y == ending[1]:
#         return cnt
#     for n in range(4):
#         nx = x + dx[n]
#         ny = y + dy[n]
#         if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and (graph[nx][ny] > cnt+1 or (nx == ending[0] and ny == ending[1])):
#             cnt += 1
#             return dfs(graph, [nx, ny], visited)
#     return 'KAKTUS'

# def bfs(graph, start, visited):
#     q = deque()
#     for s in start:
#         q.append(s)
#         visited[s[0]][s[1]] = 1
#     while q:
#         x, y = q.popleft()
#         for n in range(4):
#             nx = x + dx[n]
#             ny = y + dy[n]
#             if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and graph[nx][ny] != 'X' and graph[nx][ny] != 'D':
#                 visited[nx][ny] = visited[x][y] + 1
#                 q.append([nx, ny])
#             elif 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and graph[nx][ny] == 'D':
#                 visited[nx][ny] = R*C
#     return visited 

# visited = [[0] * C for _ in range(R)]
# x = bfs(graph, water, visited)
# waterMap = []
# for w in x:
#     waterMap.append(list(map(lambda x: x-1, w)))
# print(waterMap)
# visited = [[False] * C for _ in range(R)]
# y = dfs(waterMap, start, visited)

# print(y)