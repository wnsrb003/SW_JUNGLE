import sys
sys.stdin = open('input.txt')
from collections import defaultdict
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = defaultdict(list)
for _ in range(M):
    x,y,cost = map(int, sys.stdin.readline().split())
    graph[x].append((cost,y))
start_bus, end_bus = map(int, sys.stdin.readline().split())

def stra(start):
    distance[start] = 0
    heap = []
    heapq.heappush(heap, [distance[start], start])
    while heap:
        c_dis, c_des = heapq.heappop(heap)
        if distance[c_des] < c_dis:
                continue
        for a in graph[c_des]:
            new_dis = a[0]
            new_des = a[1]
            if new_dis + c_dis < distance[new_des]:
                distance[new_des] = new_dis + c_dis
                heapq.heappush(heap, (distance[new_des], new_des))
distance = {node: float('inf') for node in range(N+1)}
stra(start_bus)
print(distance[end_bus])