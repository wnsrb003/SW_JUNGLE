import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)
M, N = map(int, sys.stdin.readline().split())
boxs = []
for _ in range(N):
    boxs.append(list(map(int, sys.stdin.readline().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(start, visited):
    global result, boxs
    q = deque(start)
    
    while q:
        i,j = q.popleft()
        # visited[i][j] = 1
        for n in range(4):
            nx = i + dx[n]
            ny = j + dy[n]
            if 0 <= nx < N and 0 <= ny < M and not boxs[nx][ny]:
                # if graph[nx][ny] == 0:
                q.append((nx, ny))
                boxs[nx][ny] = boxs[i][j] + 1
                # visited[nx][ny] = visited[i][j] + 1
                result = max(result, boxs[nx][ny])

                # elif graph[nx][ny] == -1:
                #     visited[nx][ny] = -1
s = []
visited = [[0] * M for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if boxs[i][j] == 1:
            s.append((i,j))
            visited[i][j] = 1
bfs(s, visited)

for i in boxs:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
if result:
    print(result - 1)
else :
    print(0)