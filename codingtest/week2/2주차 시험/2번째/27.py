# #철로
# #https://www.acmicpc.net/problem/13334
# #우선순위큐
# import sys
# import heapq

# # n = 8
# # 철로 = [[5,40], [25,35], [10,20], [10,25], [30,50], [50,60], [25,30], [80,100]]
# # d = 30

# n = int(sys.stdin.readline().strip())
# 철로 = []
# for i in range(n) :
#     x = list(map(int, sys.stdin.readline().strip().split()))
#     if x[1]<x[0]:
#         x = [x[1], x[0]]
#     철로.append(x)
# d = int(sys.stdin.readline().strip())

# sorted(철로, key = lambda i: i[1])
# 배열 = []
# 큐 = []
# 최대 = 0
# # 출퇴근 = 철로.pop()
# #heapq.heappop(배열)
# while 철로:
#     출퇴근 = 철로.pop(0)
#     if not 배열:
#         if 출퇴근[1] - 출퇴근[0] <= d:
#             # heapq.heappush(배열, [0, 출퇴근[0], 출퇴근[0]+d])
#             # 배열.append([0, 출퇴근[0], 출퇴근[0]+d])
#             # 배열.append([0, 출퇴근[1]-d, 출퇴근[1]])
#             # heapq.heappush(배열, [0, 출퇴근[1]-d, 출퇴근[1]])

#         # else :
#             heapq.heappush(배열, [출퇴근[0], 출퇴근[0]+d, 1])
#             # 배열.append([1, 출퇴근[0], 출퇴근[0]+d])
#             # 배열.append([1, 출퇴근[1]-d, 출퇴근[1]])
#             heapq.heappush(배열, [출퇴근[1]-d, 출퇴근[1], 1])
#     else :
#         flag = 0
#         뺀놈들 = []
#         if 출퇴근[1] - 출퇴근[0] <= d:
#             for _ in range(len(배열)) :
#                 뺀놈 = heapq.heappop(배열)
#                 if 뺀놈[0] <= 출퇴근[0]:
#                     if 뺀놈[1] >= 출퇴근[1]
#                         heapq.heappush(배열, [뺀놈[0], 뺀놈[1], 뺀놈[2]+1])
#                         flag += 1
#                     elif 뺀놈[1] < 출퇴근[1] and 출퇴근[1] - 뺀놈[1] >= d:
#                         heapq.heappush(배열, [뺀놈[0], 출퇴근[1], 뺀놈[2]+1])
#                         flag += 1

#                 elif 뺀놈[0] >= 출퇴근[0] and 뺀놈[1] >== 출퇴근[1]
#                 else :
#                     뺀놈들.append(뺀놈)
#             if not flag :
#                 if 출퇴근[1] - 출퇴근[0] <= d:
#                     # heapq.heappush(배열, [0, 출퇴근[0], 출퇴근[0]+d])
#                     # heapq.heappush(배열, [0, 출퇴근[1]-d, 출퇴근[1]])
#                     # break
#                 # else :
#                     heapq.heappush(배열, [1, 출퇴근[0], 출퇴근[0]+d])
#                     heapq.heappush(배열, [1, 출퇴근[1]-d, 출퇴근[1]])
#             for i in 뺀놈들:
#                 heapq.heappush(배열, i)

# if 배열 :
#     print(max([i[0] for i in 배열]))
# else :
#     print(0)


from sys import stdin
import heapq

n = int(stdin.readline())
roads, data = [], []

for _ in range(n):
    data.append(sorted(list(map(int, stdin.readline().split()))))
train_road_length = int(stdin.readline())


for road in data:
    s, e = road
    if (e - s) <= train_road_length:
        roads.append(road)

roads.sort(key=lambda x: x[1])

answer = 0
q = []

for road in roads:
    if not q:
        heapq.heappush(q, road)
    else:
        while q[0][0] < road[1] - train_road_length:
            heapq.heappop(q)
            if not q:
                break

        heapq.heappush(q, road)
    answer = max(answer, len(q))

print(answer)
