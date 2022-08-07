import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')

# def check(num):
#     if(num<2):
#         return False
#     for i in range(2, num):
#         if(num%i == 0):
#             return False
#     return True
def isitPrime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False

    return True
# n=1299710
# a = [False,False] + [True]*(n-1)
# primes=[]

# for i in range(2,n+1):
#   if a[i]:
#     primes.append(i)
#     for j in range(2*i, n+1, i):
#         a[j] = False
# print(a)
N = int(input())
for _ in range(N):
    num = int(input())
    if isitPrime(num):
        print(0)
        continue
    flag = True
    left_num = right_num = 0
    i = 1
    while not left_num:
        left_num = num - i if isitPrime(num-i) else 0
        i += 1
    i = 1
    while not right_num:
        right_num = num + i if isitPrime(num+i) else 0
        i += 1
    print(abs(left_num - right_num))
