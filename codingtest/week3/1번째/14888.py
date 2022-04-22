import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))
result = num[0]
max = -int(1e9)
min = int(1e9)
def dfs(index):
    global result, max, min
    if index == N:
        if max < result:
            max = result
        if min > result:
            min = result
    else:    
        for i in range(4):
            tmp = result
            if c[i] > 0:
                if i == 0:
                    result = result + num[index]
                elif i == 1:
                    result = result - num[index]
                elif i == 2:
                    result = result * num[index]
                else :
                    if result >= 0:
                        result = result // num[index]
                    else:
                        result =  (-result // num[index]) * -1
                c[i] -= 1
                dfs(index+1)
                result = tmp
                c[i] += 1

dfs(1)
print(max)
print(min)