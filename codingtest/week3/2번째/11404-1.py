import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

bus_cost = [[int(1e9)] * N for _ in range(N)] 
for _ in range(M):
    x, y, cost = map(int, sys.stdin.readline().split())
    bus_cost[x-1][y-1] = min(bus_cost[x-1][y-1], cost)

for k in range(N):
    bus_cost[k][k] = 0
    for i in range(N):
        for j in range(N):
            bus_cost[i][j] = min(bus_cost[i][j], bus_cost[i][k] + bus_cost[k][j])

for x in bus_cost:
    print(*x)

# dic = {'a':{'c':123}, 'b':[5,6,7]}

# def a(**dic):

