import sys
sys.stdin = open('input.txt')
n = int(input())

flo = [0]

for _ in range(n):
    flo.append(int(input()))
dp = [0 for _ in range(n+1)]


# for i in range(n):
#     if i == n-2:
#         dp[i] = [dp[i-2][0] + flo[i], 1]
#         continue
#     if dp[i-1] > dp[i-2] and dp[i-1][1] < 2:
#         dp[i] = [dp[i-1][0] + flo[i], dp[i-1][1] + 1]
#     else:
#         dp[i] = [dp[i-2][0] + flo[i], 1]
result = 0
if n == 1:
    print(flo[1])
else:    
    dp[1] = flo[1]
    dp[2] = flo[1] + flo[2]
    for i in range(3, n+1):
        dp[i] = max(dp[i-3] + flo[i-1] + flo[i], dp[i-2] + flo[i])
    print(dp[n])
# print(dp)
# print(result)



