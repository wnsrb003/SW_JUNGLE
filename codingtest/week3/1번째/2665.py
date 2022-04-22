import sys
from collections import defaultdict, deque
import heapq

sys.stdin = open('input.txt')

n = int(sys.stdin.readline())

miro = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, start_i, start_j, visited):
    visited[start_i][start_j] = 0
    queue = deque([(start_i, start_j)])

    while queue:
        i,j = queue.popleft()
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < n and 0 <= y < n:
                if visited[x][y] == -1:
                    if miro[x][y] == 0:
                        visited[x][y] = visited[i][j] + 1
                        queue.append((x,y))
                    else :
                        visited[x][y] = visited[i][j]
                        queue.appendleft((x,y))

visited = [[-1] * n for _ in range(n)] 
bfs(miro, 0, 0, visited)
print(visited[n-1][n-1])

# def dijkstra():
#     visited[0][0] = 1
#     heap = []
#     heapq.heappush(heap, (0,0,0))
#     while heap:
#         c, x, y = heapq.heappop(heap)
#         if x == n - 1 and y == n - 1:
#             print(c)
#             return
#         for i in range(4):
#             nx = x + dx[i]
#             ny = x + dy[i]
#             if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
#                 visited[nx][ny] = 1
#                 if miro[nx][ny] == 0:
#                     heapq.heappush(heap, (c+1, nx, ny))
#                 else :
#                     heapq.heappush(heap, (c, nx, ny))

def dijkstra():
    visited = [[0] * n for _ in range(n)] 
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited[0][0] = 1
    heap = []
    heapq.heappush(heap,(0,0,0))
    while heap:
        cost, x, y = heapq.heappop(heap)
        if cost > dist[x][y]:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] > cost + (miro[nx][ny] == 0):
                    dist[nx][ny] = cost + (miro[nx][ny] == 0)
                    heapq.heappush(heap, (dist[nx][ny], nx, ny))

dist = [[int(1e9)] * n for _ in range(n)]
dijkstra()
print(dist[-1][-1])        


