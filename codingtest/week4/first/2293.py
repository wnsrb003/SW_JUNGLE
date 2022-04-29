import sys
sys.stdin = open('input.txt')
n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1

for i in range(n):
    for j in range(1, k+1):
        if coins[i] <= j:
            dp[j] = dp[j-coins[i]] + dp[j]
            # print(dp[j])
# for d in dp:
print(dp[k])