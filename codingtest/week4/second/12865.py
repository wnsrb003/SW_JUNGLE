import sys

sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())

bags = [[0,0]]
for _ in range(N):
    bags.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(N+1):
    for j in range(K+1):
        if bags[i][0] <= j:
            dp[i][j] = max(dp[i-1][j-bags[i][0]] + bags[i][1], dp[i-1][j])
        else :
            dp[i][j] = dp[i-1][j]
# for d in dp:
print(dp[N][K])