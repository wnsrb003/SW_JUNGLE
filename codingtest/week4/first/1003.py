import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    dp = [(1,0), (0,1)]
    for _ in range(N-1): 
        dp.append((0,0))
    for i in range(2, N+1):
        dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])
    print(*dp[N])
