#moo게임

n = int(input())
인덱스=0
moo = 'moo'
배열 = ['']
while len(배열[0]) < n:
    if 배열[0] == '':
        배열.pop()
        배열.append(moo)
        인덱스 +=1
    else :
        뺀놈 = 배열.pop()
        오 = 'o'*인덱스
        결과 = 뺀놈+뺀놈+오+뺀놈
        # if len(뺀놈) * 3 + 인덱스 >= n:
        if len(뺀놈) * 2 >= n:
            print(뺀놈[(n-1)/2:n/2])
            break
        배열.append(결과)
        인덱스+=1