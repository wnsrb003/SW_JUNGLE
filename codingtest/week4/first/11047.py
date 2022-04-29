import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().strip().split())
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline().strip()))

coins.sort(reverse=True)
cnt = 0
for coin in coins:
    cnt += K // coin
    K = K % coin

print(cnt)