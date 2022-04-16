# 크루스칼

# import sys

# sys.stdin = open('input.txt')

# V, E = map(int, sys.stdin.readline().split())
# array = []
# result = 0
# for _ in range(E):
#     x, y, cost = map(int, sys.stdin.readline().split())
#     array.append((x, y, cost))

# array.sort(key=lambda x : x[2])

# union = [i for i in range(0, V+1)]
# def find(x):
#     if x != union[x]:
#         union[x] = find(union[x])
#     return union[x]

# for a in array:
#     x = find(a[0])
#     y = find(a[1])
#     c = a[2]
#     if x != y:
#         if union[x] > union[y]:
#             union[y] = x
#         else :
#             union[x] = y
#         result += c
# print(result)

# 프림
import sys

sys.stdin = open('input.txt')
from collections import defaultdict
import heapq

V, E = map(int, sys.stdin.readline().split())
dic = defaultdict(list)
for _ in range(E):
    x, y, cost = map(int, sys.stdin.readline().split())
    dic[x].append((cost,y))
    dic[y].append((cost,x))
visited = [False] * (V+1)
def prim(dic, start):
    q = dic[start]
    result = 0
    visited[start] = True
    heapq.heapify(q)
    while q:
        cost,y = heapq.heappop(q)
        if not visited[y]:
            visited[y] = True
            result += cost
            for a in dic[y]:
                if not visited[a[1]]:
                    heapq.heappush(q, a)
    return result

print(prim(dic, 1))