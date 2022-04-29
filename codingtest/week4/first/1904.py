import sys
sys.stdin = open('input.txt')

N = int(input())
cache = [0] * 1000001          # 왜 와이 (N+1)로 하면 인덱스에러가 나는가

cache[1] = 1
cache[2] = 2

for i in range(3, N+1):
    cache[i] = (cache[i-1] + cache[i-2]) % 15746

print(cache[N])

