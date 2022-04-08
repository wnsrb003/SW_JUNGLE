n, r, c = map(int, input().split())

global num, cnt
num = (2**n)**2
def find(N, i, j, num):
    
    if int(N) < 2:
        print(int(num - 1))
        return 
    else :
        if i < N / 2 and j < N / 2 :   # 1사분면
            # num += N*(N-6)
            num -= (N**2/4)*3
            find(N/2, i, j, num)
        if i < N / 2 and j >= N / 2 :   # 2사분면
            j = int(j - N / 2)
            # num += N*(N-4)
            num -= (N**2/4)*2
            find(N/2, i, j, num)
        if i >= N / 2 and j < N / 2 :   # 3
            i = int(i - N / 2)
            # num += N*(N-2)
            num -= (N**2/4)*1
            find(N/2, i, j, num)
        if i >= N / 2 and j >= N / 2 :  # 4
            i = int(i - N / 2)
            j = int(j - N / 2)
            num -= (N**2/4)*0
            find(N/2, i, j, num)
    return 
find(2**n, r, c, num)
