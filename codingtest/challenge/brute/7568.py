import sys
sys.stdin = open('input.txt')

n = int(input())

power = []
for _ in range(n):
    x,y = map(int, input().split())
    power.append((x,y))
result = []
for p in power:
    x, y = p
    rank = 1
    for o in power:
        x1, y1 = o
        if x < x1 and y < y1:
            rank += 1
    result.append(rank)
print(*result)