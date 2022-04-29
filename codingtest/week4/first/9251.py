import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**5)

x = list(input())
y = list(input())

n = len(x)
m = len(y)

dp = [[-1] * (m+1) for _ in range(n+1)]       # 확인 안한 값 = -1

def LCS(i, j):                      # 재귀로 풀면 시간초과.... 
    if i == 0 or j == 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]

    if x[i-1] == y[j-1]:
        # dp[i][j] = (dp[i-1][j-1] if dp[i-1][j-1] else LCS(i-1, j-1)) + 1
        dp[i][j] = LCS(i-1, j-1) + 1

    else :
        # dp[i][j] = max(dp[i-1][j] if dp[i-1][j] else LCS(i-1, j), dp[i][j-1]  if dp[i][j-1] else LCS(i, j-1))
        dp[i][j] = max(LCS(i-1, j), LCS(i,j-1))

    return dp[i][j]

LCS(n, m)
for d in dp:
    print(d)
# print(dp[n][m])
# for i in range(n):
#     for j in range(m):
#         if x[i] == y[j]:
#             dp[i+1][j+1] = dp[i][j] + 1
#         else:
#             dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
# for d in dp:
#     print(d)