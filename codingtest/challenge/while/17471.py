import sys
from collections import defaultdict, deque
from itertools import combinations
sys.stdin = open('input.txt')

def check(arg_visited):
    start = 0
    if sum(arg_visited) == 0 or sum(arg_visited) == len(arg_visited) - 1:
        return False
    for v in range(1, len(arg_visited)):
        if not arg_visited[v]:
            start = v
            break
    q = deque()
    q.append(start)
    arg_visited[start] = True
    while(q):
        pop = q.popleft()
        for i in graph[pop]:
            if not arg_visited[i]:
                q.append(i)
                arg_visited[i] = True
    for i in range(1, len(arg_visited)):
        if not arg_visited[i]:
            return False
    return True

# def dfs(index):
#     global min_cnt
#     visited[index] = True
#     arg_visited = visited[:]
#     print(*visited)

#     if check(arg_visited):
#         cnt = 0
#         for i in range(1, len(visited)):
#             if visited[i]:
#                 cnt += people[i-1]
#             else:
#                 cnt -= people[i-1]
#         min_cnt = min(min_cnt, abs(cnt))
#     for i in graph[index]:
#         if not visited[i] :
#             dfs(i)
#             visited[i] = 0


N = int(sys.stdin.readline().strip())
people = [int(i) for i in sys.stdin.readline().strip().split()]
graph = defaultdict(list)
for i in range(N):
    for index, j in enumerate(sys.stdin.readline().strip().split()):
        if index:
            graph[i+1].append(int(j))

min_cnt = 100
# for i in range(1, N+1):
#     visited = [0 for _ in range(N+1)]    
#     dfs(i)
for i in range(1, N // 2 + 1):
    combis = list(combinations(range(1, N + 1), i))
    for combi in combis:
        visited = [0 for _ in range(N+1)]
        for c in combi:
            visited[c] = True
        arg_visited1 = visited[:]
        arg_visited2 = [not i for i in arg_visited1]
        # print(arg_visited1, arg_visited2)
        if check(arg_visited1) and check(arg_visited2):
            cnt = 0
            for i in range(1, len(visited)):
                if visited[i]:
                    cnt += people[i-1]
                else:
                    cnt -= people[i-1]
            min_cnt = min(min_cnt, abs(cnt))
        # sum1, node1 = bfs(combi)
        # sum2, node2 = bfs([i for i in range(1, N + 1) if i not in combi])
        # # 두 선거구의 모든 노드가 연결되어 있는지 확인
        # if node1 + node2 == N:
        #     result = min(result, abs(sum1 - sum2))
if min_cnt == 100:
    print(-1)
else:
    print(min_cnt)