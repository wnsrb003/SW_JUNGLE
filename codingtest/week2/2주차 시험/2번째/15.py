#막대기
#https://www.acmicpc.net/problem/17608
#스택
import sys
스택 = []
n = int(sys.stdin.readline().strip())

for i in range(n):
    스택.append(int(sys.stdin.readline().strip()))

cnt = 0
큰놈 = 0 
while 스택:
    뺀놈 = 스택.pop()
    if 뺀놈 > 큰놈:
        cnt +=1
        큰놈 = max(큰놈, 뺀놈)
print(cnt)