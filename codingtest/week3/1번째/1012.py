import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)
T = int(sys.stdin.readline())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(graph, i, visited):
    visited[i[0]][i[1]] = True
    global cnt
    for n in range(4):
        nx = i[0] + dx[n]
        ny = i[1] + dy[n]
        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
            if graph[nx][ny] == 1:
                cnt += 1
                dfs(graph, (nx, ny), visited)
    if cnt: return 1
    else : return 0

def bfs(graph, start, visited):
    global cnt
    x, y = start
    q = deque([])
    visited[x][y] = False
    q.appendleft((x,y))
    while q:
        pop = q.popleft()
        for n in range(4):
            nx = pop[0] + dx[n]
            ny = pop[1] + dy[n]
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    cnt += 1
    if cnt : return 1
    else : return 0
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    visited = [[False] * N for _ in range(M)]
    graph = [[0] * N for _ in range(M)]

    for _ in range(K):
        x, y = (map(int, sys.stdin.readline().split()))
        graph[x][y] = 1
    result = 0
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1 and not visited[i][j]:
                
                cnt = 1
                result += bfs(graph, (i,j), visited)
    print(result)
    for v in visited:
        print(v)