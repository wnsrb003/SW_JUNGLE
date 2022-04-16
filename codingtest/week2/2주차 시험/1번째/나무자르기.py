# 나무자르기 https://www.acmicpc.net/problem/2805
# 이분 탐색
import sys
개수와미터, 나무들 = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(2)]

나무들.sort()
end = 나무들[-1]
start = 0
while start <= end:
    mid = (start + end) // 2
    미터 = 0
    for tree in 나무들:
        # if tree - mid > 0 :      !! 아주 간단한 연산자 한줄로 인해 시간 초과 뜸.... 신경 써야함!!!!
        if tree > mid :
            미터 += tree - mid
    if 미터 >= 개수와미터[1]:
        start = mid + 1
    else :
        end = mid - 1
print(end)
