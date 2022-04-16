#탑
#https://www.acmicpc.net/problem/2493
#스택
import sys
n = int(sys.stdin.readline().strip())
탑 = list(map(int, sys.stdin.readline().strip().split()))
결과 = [0]*n

스택 = []
for k in range(len(탑)):
    if not 스택 :
        스택.append((k, 탑[k]))
        continue
    while len(스택):
        뺄놈 = 스택[-1]
        if 뺄놈[1] > 탑[k]:
            결과[k] = 뺄놈[0] + 1
            스택.append((k, 탑[k]))
            break
        elif 뺄놈[1] == 탑[k]:
            결과[k] = 뺄놈[0] + 1
            스택.pop()
            스택.append((k, 탑[k]))
            break
        else :
            스택.pop()
            
    if not 스택:
        스택.append((k, 탑[k]))

print(' '.join(list(map(str, 결과))))
