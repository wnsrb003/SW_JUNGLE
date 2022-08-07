#https://www.acmicpc.net/problem/10870
import sys
sys.stdin = open('input.txt')

n = int(input())

def pibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return pibo(n-1) + pibo(n-2)

result = pibo(n)
print(result)