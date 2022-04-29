import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
dp = [[0] * 3 for _ in range(N)]
rgb = []

for _ in range(N):
    x,y,z = map(int, input().strip().split())
    rgb.append([x,y,z])

dp[0] = rgb[0]
n = [[1,2], [-1,1], [-2,-1]]

for i in range(1, N):
    temp = []
    rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0]
    rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1]
    rgb[i][2] = min(rgb[i-1][1], rgb[i-1][0]) + rgb[i][2]
    
print(min(rgb[N-1]))