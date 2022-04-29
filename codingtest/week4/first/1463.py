import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())

dp = [0] * (10**6+1)
dp[2] = 1
dp[3] = 1
if N < 4:
    print(dp[N])
else:
    for i in range(4, N+1):
        temp = []
        if i % 2 == 0:
            temp.append(dp[i//2] + 1)
        if i % 3 == 0:
            temp.append(dp[i//3] + 1)
        temp.append(dp[i-1] + 1)
        dp[i] = min(temp)
    print(dp[N])