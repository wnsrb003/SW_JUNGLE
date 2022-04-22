import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
        graph.append(list(map(int, list(sys.stdin.readline().strip()))))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs():
    visited[0][0][0] = 1
    q = deque()
    q.append((0,0,0))
    while q:
        x, y, delfloor = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][delfloor]
        for n in range(4):
            nx = x + dx[n]
            ny = y + dy[n]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and visited[nx][ny][delfloor] == 0:
                    visited[nx][ny][delfloor] = visited[x][y][delfloor] + 1
                    q.append((nx, ny, delfloor))
                if graph[nx][ny] == 1 and delfloor == 0:
                    visited[nx][ny][delfloor+1] = visited[x][y][delfloor] + 1
                    q.append((nx, ny, delfloor+1))
    return -1
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
print(bfs())