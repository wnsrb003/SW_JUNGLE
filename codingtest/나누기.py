A, B, C = map(int, [i for i in input().split()])
# A=10
# B=11
# C=12
flag = False
result = 1
def cnt(n):
    global result
    global flag
    if n < 1 :        
        print(result%C)
        flag = True
    else :
        result *= A % C
        cnt(n-1)
        if flag : return
cnt(B)