import sys
sys.stdin = open('input.txt')
# from math import inf

# N, M = map(int, input().split())

# cost = [[1000000000] * (N+1) for _ in range(N+1)]
# for _ in range(M):
#     i, j = map(int, input().split())
#     cost[i][j] = 1
#     cost[j][i] = 1

# for k in range(1, N+1):
#     cost[k][k] = 0
#     for i in range(1, N+1):
#         for j in range(1,N+1):
#             cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
# _max = 10000000000000000
# for i in range(1, N+1):
#     for j in range(i+1, N+1):
#         _sum = 0
#         for k in range(1, N+1):
#             _sum += min(cost[i][k], cost[j][k]) * 2
            
#         if _max > _sum:
#             _max = _sum
#             result = [i, j, _max]
# print(*result)

from itertools import combinations
from collections import deque

n, m = map(int, input().split())

nodes = [[] for _ in range(n+1)]

for _ in range(m):
    tail, head = map(int, input().split())
    nodes[tail].append(head)
    nodes[head].append(tail)
    # 무방향 그래프

cases = list(combinations([i for i in range(1, n+1)], 2))
# 모든 노드 중 두 개를 뽑는 조합

cases_score = []

for case in cases:
    queue = deque()
    visited = [False for _ in range(n+1)]
    node1, node2 = case
    queue.append([node1, 0])
    queue.append([node2, 0])
    visited[node1] = True
    visited[node2] = True
    # 루트 노드가 두 개인 그래프를 BFS
    scores = [0 for _ in range(n+1)]
    # 깊이 * 2가 해당 노드에 대한 왕복 길이
    while queue:
        cur_node, depth = queue.popleft()

        if scores[cur_node] == 0:
            scores[cur_node] = depth * 2

        for next_node in nodes[cur_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append([next_node, depth+1])
        # 모든 노드를 방문하면서 깊이 * 2를 기록한다.
    cases_score.append(scores)

result = [[sum(score), case] for score, case in zip(cases_score, cases)]
# 각 조합에 따라 깊이 합을 정리한다.

result.sort()
# 깊이 합이 최소 + 노드 번호가 작은 조합
score, nodes12 = result[0]
node1, node2 = nodes12
answer = f"{node1} {node2} {score}"
print(answer)