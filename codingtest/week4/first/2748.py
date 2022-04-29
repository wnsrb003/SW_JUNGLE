import sys
sys.stdin = open('input.txt')

N = int(input())
cache = [0] * (N+1)

# def fibo(x):
#     if x == 0 or x == 1:
#         return 1
#     if cache[x] != 0:
#         return cache[x]
#     cache[x] = fibo(x-1) + fibo(x-2)
#     return cache[x]

# print(fibo(N-1))

cache[0] = 1
cache[1] = 1

for i in range(2, N+1):                    # 왜 why N으로 하면 인덱스 에러가 나는가
    cache[i] = cache[i-1] + cache[i-2]

print(cache[N-1])

