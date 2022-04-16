import sys
sys.stdin = open('input.txt')
from collections import defaultdict, deque
N, M = map(int, sys.stdin.readline().split())

graph = defaultdict(list)
진입 = [0] * (N+1)
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    진입[y] = 진입[y] + 1

def top():
    queue = deque([])
    result = []
    for i in range(1, len(진입)):
        if 진입[i] == 0:
            queue.append(i)
    
    while queue:
        pop = queue.popleft()
        result.append(pop)
        for i in graph[pop]:
            진입[i] -= 1
            if 진입[i] == 0:
                queue.append(i)
    return result
print(' '.join(map(str, top())))

