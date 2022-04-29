import sys
sys.stdin = open('input.txt')

def fun(x, y, z):
    if x <= 0 or y <= 0 or z <=0:
        return 1

    if x > 20 or y > 20 or z > 20:
        return fun(20, 20, 20)
    
    if dp[x][y][z]:
        return dp[x][y][z]

    if x < y and y < z:
        dp[x][y][z] = fun(x, y, z-1) + fun(x, y-1, z-1) - fun(x, y-1, z)
        return dp[x][y][z]
    
    dp[x][y][z] = fun(x-1, y, z) + fun(x-1, y-1, z) + fun(x-1, y, z-1) - fun(x-1, y-1, z-1)
    return dp[x][y][z]

while True:
    # try:
    x, y, z = map(int, sys.stdin.readline().strip().split())
    if x == -1 and y == -1 and z == -1:
        break
    dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]
    print(f'w({x}, {y}, {z}) = {fun(x,y,z)}')
    # except:
        # exit()
