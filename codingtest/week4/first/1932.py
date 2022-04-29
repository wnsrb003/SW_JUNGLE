import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())

tri = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    x = list(map(int, input().strip().split()))
    for j in range(len(x)):
        tri[i][j] = x[j]

for i in range(1, N):
    for j in range(i+1):
        tri[i][j] = max(tri[i-1][j-1], tri[i-1][j]) + tri[i][j]
print(max(tri[N-1]))
