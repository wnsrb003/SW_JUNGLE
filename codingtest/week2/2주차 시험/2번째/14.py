#괄호
#https://www.acmicpc.net/problem/9012
#스택

import sys
스택 = []
결과 = []
n = int(sys.stdin.readline().strip())

for i in range(n):
    스택 = (list(sys.stdin.readline().strip()))
    cnt = 0
    flag = 1
    for _ in range(len(스택)):
        if 스택.pop() == ')':
            cnt += 1
        else :
            cnt -= 1
        if cnt < 0:
            flag = 0
            break
    if cnt == 0 and flag :
        결과.append('YES')
    else :
        결과.append('NO')

print('\n'.join(결과))