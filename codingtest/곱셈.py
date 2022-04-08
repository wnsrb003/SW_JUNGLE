# 곱셈 https://www.acmicpc.net/problem/1629
# 분할 정복으로 풀어보기

def 나누기(n):
    if n == 1:
        return A%C
    else :
        tmp = 나누기(n//2)
        if n%2 == 1:
            return (tmp * tmp * A)%C
        else :
            return (tmp * tmp)%C
        return

import sys
A,B,C = list(map(int, sys.stdin.readline().strip().split()))
print(나누기(B))