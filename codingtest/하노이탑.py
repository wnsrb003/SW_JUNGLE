n = int(input())
x = 1
y = 3
cnt = 0

def move(n, x, y):
    global cnt

    if n == 1:
        cnt+=1
        print(f"{x} {y}")
    else :
        cnt+=1
        move(n-1, x, 6-x-y)
        print(f"{x} {y}")
        move(n-1, 6-x-y, y)
        
if n > 20:
    print(2**n+1)
else : 
    print(2*(n-1)+1)
    move(n, x, y) 