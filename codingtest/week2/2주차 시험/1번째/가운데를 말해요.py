import sys
import heapq
# import copy

# 힙배열 = []
# 임시힙배열 = []
# 숫자개수 = int(sys.stdin.readline().strip())

# for i in range(숫자개수):
#     숫자 = int(sys.stdin.readline().strip())
#     힙배열 = copy.deepcopy(임시힙배열)
#     결과 = []
#     heapq.heappush(힙배열, 숫자)
#     heapq.heappush(임시힙배열, 숫자)
#     for i in range(len(힙배열)):
#         결과.append(heapq.heappop(힙배열))
#     힙길이 = len(결과)
#     if 힙길이 < 1 :
#         sys.stdout.write(str(결과[0]))
#         continue
#     if 힙길이 == 2 :
#         sys.stdout.write(str(min(결과[0], 결과[1])))
#     elif 힙길이%2 == 0:
#         sys.stdout.write(str(min(결과[힙길이//2 - 1], 결과[힙길이//2])))
#     else :
#         sys.stdout.write(str(결과[힙길이//2]))

최대힙배열 = []
최소힙배열 = []
결과 = []
숫자개수 = int(sys.stdin.readline().strip())

for i in range(숫자개수):
    숫자 = int(sys.stdin.readline().strip())
    if len(최대힙배열) == len(최소힙배열):
        heapq.heappush(최대힙배열, (-숫자, 숫자))
    else :
        heapq.heappush(최소힙배열, (숫자, 숫자))

    if 최소힙배열 and 최대힙배열[0][1] > 최소힙배열[0][0] :
        최소 = heapq.heappop(최소힙배열)[0]
        최대 = heapq.heappop(최대힙배열)[1]
        heapq.heappush(최대힙배열, (-최소, 최소))
        heapq.heappush(최소힙배열, (최대, 최대))
    
    if len(최대힙배열) == len(최소힙배열):
        결과.append(min(최대힙배열[0][1], 최소힙배열[0][1]))
    else :  
        결과.append(최대힙배열[0][1])
for r in 결과:
    print(r)