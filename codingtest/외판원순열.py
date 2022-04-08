from itertools import permutations as p
import sys
def a():
    n = int(sys.stdin.readline().strip())

    citys = [i for i in range(1, n+1)]
    prices = [[]]

    for i in range(1, n+1):
        inp = sys.stdin.readline().strip().split()
        array = [0]
        for j in inp:
            array.append(j)
        prices.append(list(map(int, array)))

    paths = list(p(citys, n))
    min_price = 100000000

    for i in paths:
        path = list(i)
        if prices[path[-1]][path[0]] == 0:
            continue
        path.append(path[0])

        cnt = 0
        

        for j in range(len(path)-1):
            if prices[path[j]][path[j+1]] == 0:
                cnt = 100000000
                break
            else :
                cnt += prices[path[j]][path[j+1]]
            if cnt >= min_price:
                cnt = 100000000
                break   
        if min_price > cnt:
            min_price = cnt

    print(min_price)
a()