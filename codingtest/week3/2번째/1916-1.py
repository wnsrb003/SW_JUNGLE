import sys
from collections import defaultdict
import heapq

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = defaultdict(list)

for _ in range(M):
    x, y, cost = map(int, sys.stdin.readline().split())
    graph[x].append((cost, y))

start_bus, end_bus = map(int, sys.stdin.readline().split())

cost = [int(1e9)] * (N+1)
def stra(graph, start):
    cost[start] = 0
    heap = [[cost[start], start]]
    heapq.heapify(heap)
    while heap:
        cur_cost, cur_des = heapq.heappop(heap)
        if cur_cost > cost[cur_des]:
            continue
        for i in graph[cur_des]:
            new_cost, new_des = list(i)
            if cost[new_des] > cur_cost + new_cost:
                cost[new_des] = cur_cost + new_cost
                heapq.heappush(heap, [cost[new_des], new_des])
stra(graph, start_bus)
print(cost[end_bus])