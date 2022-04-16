# https://www.acmicpc.net/problem/10828
# 스택
import sys
n = int(sys.stdin.readline().strip())

stack = []

for _ in range(n):
    inp = sys.stdin.readline().strip().split()
    if 'push' in inp:
        stack.append(inp[1])
    elif 'top' in inp:
        if len(stack):
            print(stack[-1])
        else :
            print(-1)
    elif 'pop' in inp:
        if len(stack):
            print(stack[-1])
            stack.pop()
        else :
            print(-1)
    elif 'size' in inp:
        print(len(stack))
    else :
        if len(stack):
            print(0)
        else :
            print(1)
    