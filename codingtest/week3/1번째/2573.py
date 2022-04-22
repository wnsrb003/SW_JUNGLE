import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**4)
from collections import defaultdict, deque
N, M = map(int, sys.stdin.readline().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

# def count_iceberg(start_x, start_y):
#     q = deque()
#     q.append((start_x, start_y))
#     ice_visited[start_x][start_y] = True
#     cnt = 1
#     while q:
#         x, y = q.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 0 and not ice_visited[nx][ny]:
#                 ice_visited[nx][ny] = True
#                 q.append((nx, ny))
#                 cnt += 1
#     return cnt 
def dfs(graph, i, visited):
    x, y = i
    visited[x][y] = True
    nexts = []
    for n in range(4):
        nx = x + dx[n]
        ny = y + dy[n]
        if 0 <= nx < N and 0 <= ny < M:
            if not graph[nx][ny] and not visited[nx][ny]:
                if graph[x][y] == 0:
                    graph[x][y] = 0
                else:
                    graph[x][y] -= 1
            elif graph[nx][ny] and not visited[nx][ny] :
                nexts.append((nx,ny))
            if not graph[x][y]:
                visited[x][y] = True
    for n in nexts:
        if not visited[n[0]][n[1]]:
            dfs(graph, n, visited)

cnt = 0
check = 0
while True:
    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                visited = [[False] * M for _ in range(N)]
                cnt += 1
                dfs(graph, (i,j), visited)
                check += 1
                # ice_visited = [[False] * M for _ in range(N)]
                # ice_total_cnt = 0
                # for x in range(N):
                #     for y in range(M):
                #         if graph[x][y]:
                #             ice_total_cnt += 1

                # for x in range(N):
                #     for y in range(M):
                #         if graph[x][y] and not ice_visited[x][y]:
                #             ice = count_iceberg(x,y)
                #             if ice != ice_total_cnt:
        if check > 1:
            print(cnt -1)
            exit(0)