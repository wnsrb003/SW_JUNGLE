import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    stocks = list(map(int, sys.stdin.readline().strip().split()))
    values = []
    max_p = 0
    total = 0
    for s in range(len(stocks)-1, -1, -1):
        if max_p < stocks[s]:
            max_p = stocks[s]

        else:
            values.append(stocks[s])
            total += max_p - stocks[s]
    print(total)
