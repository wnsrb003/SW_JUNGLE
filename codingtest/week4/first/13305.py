import sys
sys.stdin = open('input.txt')
n = int(input())
dis = list(map(int, input().split()))
prices = list(map(int, input().split()))

result = 0
m = prices[0]
for i in range(n-1):
    if prices[i] < m:
        m = prices[i]
        result += m * dis[i]
        continue
    result += m * dis[i]

print(result)