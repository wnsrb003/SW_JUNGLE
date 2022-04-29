import sys
sys.stdin = open('input.txt')
n = int(input())

l = list(map(int, input().split()))

l.sort()

result = 0
for i in range(len(l)):
    result += l[i] + sum(l[:i])
print(result)