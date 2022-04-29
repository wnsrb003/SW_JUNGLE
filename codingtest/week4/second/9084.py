import sys

sys.stdin = open('input.txt')

T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    coins = list(map(int, sys.stdin.readline().strip().split()))
    M = int(sys.stdin.readline().strip())
    
    dp = [0] * (M+1)
    dp[0] = 1
    for coin in coins:
        for i in range(1, M+1):
            if i >= coin:
                # if i % coin == 0:
                    dp[i] = dp[i-coin] + dp[i]
    print(dp[M])
