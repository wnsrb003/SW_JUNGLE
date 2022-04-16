# 수찾기 https://www.acmicpc.net/problem/1920
# 이분탐색

def find(value, start, end):
    mid = (end + start)//2
    if n[mid] == value:
        print(1)
        return
    else :
        if end == start :
            print(0)
            return
        if n[mid] < value:
            start = mid + 1
        else :
            end = mid
        find(value, start, end)

import sys
N = int(input())
n = list(map(int, sys.stdin.readline().strip().split()))
M = int(input())
m = list(map(int, sys.stdin.readline().strip().split()))
n.sort()

for i in m:
    if n[-1] < i or n[0] > i:
        print(0)
        continue
    find(i, 0, len(n)-1)




