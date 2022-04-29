import sys
import heapq
sys.stdin = open('input.txt')

N,K = map(int, input().split())

jew = []

for _ in range(N):
    wei, pri = map(int, input().split())
    jew.append([wei, pri])
jew.sort(reverse=True)

max_wei = []
for _ in range(K):
    max_wei.append(int(input()))
max_wei.sort(reverse=True)

bag = []

for i in range(len(jew)):
    if jew[i][0] <= max_wei[0]:
        heapq.heappush(bag, -jew[i][1])




# bag = []
# if K == 0:
#     print(0)
# else:
#     for i in range(len(jew)):
#         if len(bag) > K:
#             break
#         if jew[i][1] <= max_wei:
#             bag.append(jew[i][0])
#     print(sum(bag))