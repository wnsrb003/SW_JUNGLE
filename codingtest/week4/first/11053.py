import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().strip().split()))

dp =  [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if array[j] < array[i] :
            dp[i] = max(dp[j] + 1, dp[i])
        

print(max(dp))