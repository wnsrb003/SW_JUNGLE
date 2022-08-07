import sys
sys.stdin = open('input.txt')

n = int(input())
result = 0
for i in range(n):
    if i + sum(map(int, list(str(i)))) == n:
        result = i
        break

print(result)