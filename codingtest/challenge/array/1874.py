#https://www.acmicpc.net/problem/1874
import sys
sys.stdin = open('input.txt')

num = int(input())
cnt = 0
result = []
stack = []
flag = True
for _ in range(num):
    inp = int(input())
    while inp > cnt:
        cnt += 1
        result.append('+')
        stack.append(cnt)
    if inp == stack[-1]:
        stack.pop()
        result.append('-')
    else:
        flag = False
        break
if flag:
    for r in result:
        print(r)
else :
    print('no')