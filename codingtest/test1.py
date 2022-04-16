import heapq
import sys

n = int(input())
배열 = []
for i in range(n):
    배열.append(int(input()))

최소힙 = []
최대힙 = []

for i in range(len(배열)):
    if len(최대힙) != len(최소힙):
        heapq.heappush(최소힙, (배열[i], 배열[i]))
    else:
        heapq.heappush(최대힙, (-배열[i], 배열[i]))
    
    while 최대힙[0][1] > 최소힙[0][1]:
        a = heapq.heappop(최대힙)
        b = heapq.heappop(최소힙)
        heapq.heappush(최소힙, a)
        heapq.heappush(최대힙, b)
    print(min(최대힙[0][1], 최소힙[0][1]))

    