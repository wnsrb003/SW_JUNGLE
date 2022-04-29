import sys
sys.stdin = open('input.txt')
n = int(input())

a = list(map(int, input().split()))
dp = [0] * n
dp[0] = a[0]

for i in range(1, n):
    # sum_list.append(max(sum_list[i] + a[i], a[i]))
    dp[i] = max(dp[i-1]+ a[i], a[i])
print(max(dp))

