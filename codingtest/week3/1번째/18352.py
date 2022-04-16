import sys
sys.stdin = open('input.txt')
from collections import defaultdict, deque

N, M, K, X = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for i in range(M):
    x, y = list(map(int, sys.stdin.readline().split()))
    graph[x].append(y)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    result = []
    dis[start] = 0
    while queue:
        pop = queue.popleft()
        for i in graph[pop]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                dis[i] = dis[pop] + 1
                if dis[i] == K:
                    result.append(i)
    if not len(result) :
        print(-1)
    else :
        result.sort()
        for i in result:
            print(i, end='\n')

visited = [False] * (N+1)
dis = [0] * (N+1)
bfs(graph, X, visited)