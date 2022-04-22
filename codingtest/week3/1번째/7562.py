import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')

def bfs(graph, start, end):
    i, j = start
    graph[i][j] = 1
    q = deque()
    q.append([i, j])
    while q:
        x, y = q.popleft()
        if x == end[0] and y == end[1]:
            return graph[x][y]
        for n in range(8):
            nx = x + dx[n]
            ny = y + dy[n]
            if 0 <= nx < L and 0 <= ny < L and not graph[nx][ny]:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])
    return -1

T = int(sys.stdin.readline())
for _ in range(T):
    L = int(sys.stdin.readline())
    start = list(map(int,sys.stdin.readline().split()))
    end = list(map(int,sys.stdin.readline().split()))
    graph = [[0] * L for _ in range(L)]
    dx = [-2, -2, 1, -1, 2, 2, -1, 1]
    dy = [1, -1, -2, -2, -1, 1, 2, 2]
    
    print(bfs(graph, start, end)-1)
    


