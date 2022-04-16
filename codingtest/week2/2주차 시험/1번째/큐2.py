# https://www.acmicpc.net/problem/18258
# 큐
import sys
from collections import deque
n = int(sys.stdin.readline().strip())

queue = deque()

for _ in range(n):
    inp = sys.stdin.readline().strip().split()
    if 'push' in inp:
        queue.append(inp[1])
    elif 'front' in inp:
        if len(queue):
            print(queue[0])
        else :
            print(-1)
    elif 'back' in inp:
        if len(queue):
            print(queue[-1])
        else :
            print(-1)
    elif 'pop' in inp:
        if len(queue):
            print(queue[0])
            queue.popleft()
        else :
            print(-1)
    elif 'size' in inp:
        print(len(queue))
    else :
        if len(queue):
            print(0)
        else :
            print(1)
    