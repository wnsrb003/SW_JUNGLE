#뱀
#https://www.acmicpc.net/problem/3190
#큐
import sys
from collections import deque

n = int(sys.stdin.readline().strip())
사과 = []
for i in range(int(sys.stdin.readline().strip())):
    사과.append(list(map(int, sys.stdin.readline().strip().split())))

방향 = [0, 1, 2, 3]
방향변경 = deque()   #1 = 우, 2=아래, 3=좌, 4=위
for i in range(int(sys.stdin.readline().strip())):
    방향변경.append(list(map(str, sys.stdin.readline().strip().split())))
    
현재방향 = 0
먹은사과 = 0
뱀 = deque([[1,1]])
초 = 0
while True:
    초 += 1
    if 현재방향 == 0:
        위치 = [뱀[-1][0], 뱀[-1][1] + 1]
    elif 현재방향 == 1:
        위치 = [뱀[-1][0] + 1, 뱀[-1][1]] 
    elif 현재방향 == 2:
        위치 = [뱀[-1][0], 뱀[-1][1] - 1]
    else :
        위치 = [뱀[-1][0] - 1, 뱀[-1][1]]

    if 위치[0] == n+1 or 위치[1] == n+1 or not 위치[0] > 0 or not 위치[1] > 0:
        break
    elif 뱀 and 위치 in 뱀:
        break
    else :
        if 방향변경 and 초 == int(방향변경[0][0]):
            if 'D' == 방향변경[0][1]:
                if 현재방향 == 3:
                    현재방향 = 방향[0]    
                else :
                    현재방향 = 방향[현재방향+1]
            else :
                현재방향 = 방향[현재방향-1]
            방향변경.popleft()
        뱀.append(위치)
        if 사과 and 위치 in 사과:
            사과.remove(위치)
        else :
            뱀.popleft()
print(초)