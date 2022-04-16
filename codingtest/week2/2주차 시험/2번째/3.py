# 공유기 https://www.acmicpc.net/problem/2110
# 이분탐색
import sys
n, c = list(map(int, sys.stdin.readline().strip().split()))
집 = []
for i in range(n):
    집.append(int(sys.stdin.readline().strip()))
집.sort()
최대 = (집[-1] - 집[0])
최소 = 1
최대거리 = 0

def 거리재기(minn, maxx):
    global 최대거리
    if minn > maxx:
        return 
    mid = (minn+maxx)//2
    # 공유기수 = c - 1
    # for i in range(1, len(집)):
    #     if 집[i] - 집[0] >= mid:
    #         공유기수 -= 1
    #         if (집[-1] - 집[i]) >= mid * 공유기수:
    #             최대거리 = max(최대거리, mid)
    #             거리재기(mid+1, maxx)
    #             break
    #         else :
    #             거리재기(minn, mid-1)
    #             break            
    공유기수 = 1
    현재 = 집[0]
    for i in range(1, len(집)):
        if 집[i] - 현재 >= mid:
            공유기수 += 1
            현재 = 집[i]
    if 공유기수 >= c:
        최대거리 = max(최대거리, mid)
        거리재기(mid+1, maxx)
    else :
        거리재기(minn, mid-1)
if c == 2:
    최대거리 = 최대
else: 
    거리재기(1, 최대)
print(최대거리)
