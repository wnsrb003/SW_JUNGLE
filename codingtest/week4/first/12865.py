import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**5)

N, K = map(int, sys.stdin.readline().strip().split())

w = [0]
v = [0]
for _ in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    w.append(x)
    v.append(y)

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(K+1):
        if w[i] <= j:
            dp[i][j] = max(dp[i-1][j-w[i]]+v[i], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])
# for d in dp:
#     print(d)

