n = int(input())
board = [0] * n
flag_a = [False] * n
flag_b = [False] * (2*n - 1) #오 위, 왼 아
flag_c = [False] * (2*n - 1)#왼 위, 우 아
cnt = 0

def set(i):
    for j in range(n):
        if not flag_a[j] \
            and not flag_b[i+j] \
            and not flag_c[i-j+n-1]:
            if i == n - 1:
                global cnt
                cnt+=1
            else :
                board[i] = j
                flag_a[j] = True 
                flag_b[i+j] = True
                flag_c[i-j+n-1] = True
                set(i+1)
                board[i] = ''
                flag_a[j] = False
                flag_b[i+j] = False
                flag_c[i-j+n-1] = False


# def put():
#     if '' not in board:
#         for i in range(len(board)):
#             print(f'{board[i]:2}', end='')

set(0)
print(cnt)