from itertools import permutations as p
import sys

n = sys.stdin.readline().strip()
list_num = list(map(int, sys.stdin.readline().strip().split()))
a = ['+', '-', '*', '/']
list_a = sys.stdin.readline().strip().split()
list_b = []
for i in range(len(list_a)):
    if int(list_a[i]) > 0:
        for _ in range(int(list_a[i])):
            list_b.append(a[i])

comb = list(map(list, p(list_b, len(list_b))))
min = 10000000000000000000000
max = -1000000000000000000000
for i in range (len(comb)):
    result = list_num[0]
    for j in range (len(comb[i])):
        if comb[i][j] == '+':
            result = result + list_num[j+1]
        if comb[i][j] == '-':
            result = result - list_num[j+1]
        if comb[i][j] == '*':
            result = result * list_num[j+1]
        if comb[i][j] == '/':

    if result > max :
        max = result
    if result < min :
        min = result
print(max)
print(min)
