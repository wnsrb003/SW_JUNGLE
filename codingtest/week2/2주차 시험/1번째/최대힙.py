# 최대힙 https://www.acmicpc.net/problem/11279
# 힙 정렬

import sys
import heapq

힙배열 = []
결과 = []
입력수 = int(sys.stdin.readline().strip())

for i in range(입력수):
    입력값 = int(sys.stdin.readline().strip())
    if 입력값 == 0 :
        if 힙배열 :
            print(0 - 힙배열[0])
            heapq.heappop(힙배열)
        else :
            print(0)
    else :
        heapq.heappush(힙배열, 0 - 입력값)
        