import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')
M, N, H = map(int,sys.stdin.readline().strip().split())
boxs = []
visited = []
for _ in range(H):
    for _ in range(N):
        boxs.append(list(map(int, sys.stdin.readline().strip().split())))
        visited.append([False] * M)

def bfs(start):
    dx = [-1, 0, 0, 1, N, -N]
    dy = [0, -1, 1, 0, 0, 0]
    queue = deque(start)
    result = 0
    while queue:
        len_q = len(queue)
        for _ in range(len_q):
            cnt = 0
            x,y = queue.popleft()
            visited[x][y] = True
            for i in range(6):
                if i == 0 and x%N == 0:
                    continue
                if i == 3 and x%N == N-1:
                    continue
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N*H and 0 <= ny < M:
                    if not visited[nx][ny]:
                        if boxs[nx][ny] == -1:
                            visited[nx][ny] = True
                        elif boxs[nx][ny] == 1:
                            visited[nx][ny] = True
                            # queue.append((nx,ny))
                            # cnt += 1
                        else:
                            visited[nx][ny] = True
                            queue.append((nx,ny))
                            cnt += 1
        if cnt : result += 1
    return result
start = []
for i in range(N * H):
    for j in range(M):
        if boxs[i][j] == 1:
            start.append((i,j))
result = bfs(start)


for i in range(H):
    for j in range(N):
        if not visited[i][j]:
            if boxs[i][j] == 1:
                continue
            else :
                result = -1
print(result)
