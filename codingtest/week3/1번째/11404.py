import sys

sys.stdin = open('input.txt')
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
dp = [[int(1e9)] * (n) for _ in range(n)]

for _ in range(m):
    x, y, cost = map(int, sys.stdin.readline().split())
    dp[x-1][y-1] = min(dp[x-1][y-1], cost)

# k : 경유지
for k in range(n):
    dp[k][k] = 0
	# i : 출발지
    for i in range(n):
        # j : 목적지
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
for row in dp:
    for i in range(n):
        if row[i] == int(1e9):
            row[i] = 0
        print(row[i], end=' ')
    print()