# 사냥꾼
# https://www.acmicpc.net/problem/8983
# 이분탐색

import sys
import heapq
사대수, 동물수, 사정거리 = list(map(int, sys.stdin.readline().strip().split()))
사대 = list(map(int, sys.stdin.readline().strip().split()))
사대.sort()
동물 = []
for i in range(동물수):
    동물.append(((list(map(int, sys.stdin.readline().strip().split())))))
# 동물 = [(7,2), (3,3), (4,5), (5,1), (2,2), (1,4), (8,4), (9,4)]


def 찾기(x, start, end):
    최소차이 = (-1, float('inf'))
    while start <= end:
        mid = (start+end)//2
        if 사대[mid] == x:
            return x
        else:
            if 사대[mid] < x:
                start = mid + 1
            else:
                end = mid - 1
        if 최소차이[1] > abs(사대[mid] - x):
            최소차이 = (mid, abs(사대[mid] - x))

    mid = 최소차이[0]
    return 사대[mid]


cnt = 0
for i in 동물:
    if i[0] < 사대[0] - 사정거리 or i[0] > 사대[-1] + 사정거리 :
        continue
    if i[1] > 사정거리:
        continue
    가까운사대 = 찾기(i[0], 0, len(사대)-1)
    if abs(가까운사대 - i[0]) + i[1] <= 사정거리:
        cnt += 1
print(cnt)
