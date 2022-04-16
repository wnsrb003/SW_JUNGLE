#제로 https://www.acmicpc.net/problem/10773
#스택

import sys
n = int(sys.stdin.readline().strip())

stack = []
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    if num :
        stack.append(num)
    else :
        stack.pop()

print(sum(stack))
