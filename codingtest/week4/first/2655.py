import sys
import copy
sys.stdin = open('input.txt')
N = int(sys.stdin.readline())

blocks = [[0,0,0,0]]
for i in range(N):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    blocks.append([i+1, a, b, c])
blocks.sort(key=lambda x:x[1])

dp = [0 for _ in range(N+1)]
# cnt_height = [[] for _ in range(N)]
# index_blocks = [[] for _ in range(N)]

for i in range(1, N+1):
    for j in range(0, i):
        if blocks[i][3] > blocks[j][3]:
            dp[i] = max(dp[i], dp[j] + blocks[i][2])
max_h = max(dp)
# print(max_h)
max_index = dp.index(max_h)
result = []
while max_index != 0:
    if max_h == dp[max_index]:
        result.append(blocks[max_index][0])
        max_h -= blocks[max_index][2]
    max_index -= 1
print(len(result))
for i in range(len(result)-1, -1, -1):
    print(result[i])
# cnt.sort(key=lambda sum(x): x[1])
# max_h = 0
# max_index = 0
# for i in range(N):
#     max_temp = sum(cnt_height[i])
#     if max_temp >= max_h:
#         max_h = max_temp
#         max_index = i
# cnt = len(index_blocks[max_index])
# print(cnt)
# for _ in range(cnt):
#     print(index_blocks[max_index].pop() + 1)
