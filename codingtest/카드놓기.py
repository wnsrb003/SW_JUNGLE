n = int(input())
k = int(input())
num = []
for i in range(n):
    num.append(int(input()))

result = set()
comb = []
picked = [False] * n
def cho(N):
    if N == k:
        result.add(''.join(map(str, comb)))
        return
    for i in range(n):
        if not picked[i]:
            # if len(comb) < k:
                comb.append(num[i])
                picked[i] = True
                cho(N+1)
                comb.pop()
                picked[i] = False
cho(0)
print(len(result))

# comb = 

# from itertools import *

# n, k = int(input()), int(input())
# card = []
# for i in range(n):
#     card.append(int(input()))

# res = set()
# for i in list(permutations(card, k)):
#     res.add(''.join(list(map(str, i))))
# print(len(res))