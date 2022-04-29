import sys
sys.stdin = open('input.txt')
from collections import defaultdict
import operator
N = int(sys.stdin.readline().strip())

# meets = defaultdict(list)
temp = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    
    temp.append((x,y))
    # meets[x].append(y)
temp = sorted(temp, key = lambda x: (x[1], x[0]))
# for i in temp:
#     meets[i[0]].append(i[1])

cnt = 1
end = temp[0][1]
for i in range(1, N):
    if temp[i][0] >= end:
        cnt += 1
        end = temp[i][1]
print(cnt)
# for i in range(N):
#     new_cnt = 1
#     start = i
#     for j in range(i+1, N):
#         if temp[j][0] >= temp[start][1]:
#             new_cnt += 1
#             start = j
#     cnt = max(cnt, new_cnt)

