# 히오스 프로게이머
# https://www.acmicpc.net/problem/16564
# 이분탐색

n, k = list(map(int, input().split()))
레벨 = []
for _ in range(n):
    레벨.append(int(input()))
# n, k = [3, 10]
# 레벨 = [10,20,15]
레벨.sort()
start = 레벨[0]
end = 레벨[-1] + k
최대레벨 = 0

while(start<=end):
    mid = (start+end)//2
    cnt = 0
    for i in range(len(레벨)):
        if 레벨[i] < mid:
           cnt += mid - 레벨[i]
    if cnt > k:
            end = mid - 1
    else :
        최대레벨 = max(최대레벨, mid)
        start = mid + 1

print(최대레벨)