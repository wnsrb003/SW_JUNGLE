#히스토그램에서 가장 큰 직사각형 
# https://www.acmicpc.net/problem/6549
# 스택
import sys
import copy

# 테스트 = [[2,1,4,5,1,3,3], [1000, 1000, 1000,1000]]
n = []
while True:
    inp = sys.stdin.readline().strip().split()
    if '0' == inp[0]:
        break
    n.append(list(map(int, inp))[1:])

for 그램 in n:
    스택 = []   
    idx = 0 
    최대너비 = 0
    for i in range(len(그램)):
        인덱스 = idx
        if not 스택 :
            스택.append((idx, 그램[i]))
            idx += 1
            continue
        
        while 스택:
            막스택 = 스택[-1]
            if 그램[i] == 막스택[1]:
                break

            if 그램[i] < 막스택[1]:
                최대너비 = max(최대너비, 막스택[1] * (idx - 막스택[0]))
                인덱스 = 스택.pop()[0]
            else :
                스택.append((인덱스, 그램[i]))
                break   
        if not 스택:
            스택.append((인덱스, 그램[i])) 
        idx += 1    
    if 스택:
        now_idx = len(그램)
        for ele in 스택:
            idx, h = ele
            최대너비 = max((now_idx - idx) * h, 최대너비)
    print(최대너비)