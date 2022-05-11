# https://www.acmicpc.net/problem/17298
import sys
sys.stdin = open('input.txt')

n = int(input())
arr = list(map(int, input().split()))
result = [-1]* (n-1)
stack = []
for i in range(n):
    if not stack:
        stack.append(i)
        continue
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    stack.append(i)
result.append(-1)
print(*result)