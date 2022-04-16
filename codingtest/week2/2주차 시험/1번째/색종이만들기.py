# 색종이 만들기 https://www.acmicpc.net/problem/2630
# 분할정복으로 풀어보기

def 자르기(n, x, y):
    if n == 1 :
        result[색종이[x][y]] += 1
    else :
        color = 색종이[x][y]
        flag = True
        for i in range(x, x+n):
            for j in range(y, y+n):
                if 색종이[i][j] != color:
                   flag = False 
                   break
            if not flag :
                break
        if flag :
            result[color] += 1
        else :
            자르기(n//2, x, y)
            자르기(n//2, x, y+n//2)
            자르기(n//2, x+n//2, y)
            자르기(n//2, x+n//2, y+n//2)

import sys
n = int(input())
색종이 = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
result = [0]*2
자르기(n, 0, 0)                    
print('\n'.join(map(str, result)))