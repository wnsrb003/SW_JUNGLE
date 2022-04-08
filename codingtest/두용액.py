#https://www.acmicpc.net/problem/2470
#이진탐색
import sys
n, 용액들 = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(2)]

용액들.sort()
start = 0
end = len(용액들) - 1
결과 = [1000000000, 1000000000, 2000000000]
while start < end :
    혼합용액 = 용액들[start] + 용액들[end]
    if 혼합용액 == 0 :
        결과[0], 결과[1], 결과[2] = (용액들[start], 용액들[end], 혼합용액)
        break
    else :
        if abs(결과[2]) > abs(혼합용액):
            결과[0], 결과[1], 결과[2] = (용액들[start], 용액들[end], 혼합용액)
        if 혼합용액 < 0:
            start += 1
        else :
            end -= 1
print(' '.join(list(map(str, 결과[:2]))))