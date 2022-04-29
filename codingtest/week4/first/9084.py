import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    coins = list(map(int, sys.stdin.readline().strip().split()))
    count = int(sys.stdin.readline().strip())
    memo = [0] * (count+1)
    memo[0] = 1
    for coin in coins:
        for i in range(1, count+1):
            if i >= coin:
                memo[i] += memo[i-coin]

    print(memo[count])