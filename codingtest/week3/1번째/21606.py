import sys
from collections import defaultdict
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
space = list(map(int, list('0' + sys.stdin.readline().strip())))

graph = defaultdict(list)
try:
    while(True):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
except:
    pass
result = 0

def dfs(graph, index, visited):
    cnt = 0
    visited[index] = True
    for i in graph[index]:
        if space[i] == 1:
            cnt += 1
            visited[i] = True
        else:
            if not visited[i]:
                cnt += dfs(graph, i, visited)
    return cnt

visited = [False] * (N+1)
for i in range(1, len(space)):
    if space[i] == 0:
        if not visited[i]:
            cnt = dfs(graph, i, visited)
            result += cnt*(cnt-1)
    else :
        for j in graph[i]:
            if space[j] == 1:
                result += 1
print(visited)
print(result)
# for i in range(1, len(visited)):
#     if visited[i]
# def dfs(graph, index, visited):
#     global cnt
#     visited[index] = True
#     for i in graph[index]:
#         if not visited[i]:
#             if space[i] != 1:
#                 dfs(graph, i, visited)
#             else:
#                 cnt += 1        
# for i in range(1, len(space)):
#     visited = [False] * (N+1)
#     if space[i] == 1:
#         dfs(graph, i, visited)
print(cnt)