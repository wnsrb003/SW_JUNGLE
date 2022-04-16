n = input()
k = ['P', 'P', 'A', 'P']
스택 = []

if n == 'P' or n == 'PPAP':
    print('PPAP')
else :        
    for i in n:
        스택.append(i)
        if 스택[-4:] == k:
            for _ in range(4):
                스택.pop()
            if len(스택) == 1 or 스택 == ['P']:
                print('PPAP')
            else :
                print('NP')
