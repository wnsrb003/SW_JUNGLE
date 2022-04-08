# n=4
# city = [1,2,3,4]
# price = [[0,0,0,0,0], [0, 0, 10, 15, 20], [0, 5, 0, 9, 10], [0, 6, 13, 0, 12], [0, 8, 8, 9, 0]]
import sys
n=int(sys.stdin.readline().strip())
city = [i for i in range(1, n+1)]
price = [[]]
for i in range(1, n+1):
        inp = sys.stdin.readline().strip().split()
        array = [0]
        for j in inp:
            array.append(j)
        price.append(list(map(int, array)))

route = []
visited = []
path = []
min_price = 500000000
def travel(idx):
    global min_price
    if idx > n:
        cnt = 0
        # print(path)
        if price[path[-1]][path[0]] == 0:
            return
        for i in range(len(path)):
            cnt += price[path[i-1]][path[i]]
            if cnt > min_price :
                continue
        min_price = min(min_price, cnt)
    else :
        for j in city:
            if not j in visited:
                if len(path) > 0 and price[path[len(path)-1]][j] == 0:
                    continue
                else:
                    path.append(j)
                    visited.append(j)
                    travel(idx+1)
                    path.remove(j)
                    visited.remove(j)

travel(1)
print(min_price)