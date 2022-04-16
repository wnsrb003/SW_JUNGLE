import sys
그램 = []
while True:
    inp = sys.stdin.readline().strip().split()
    if '0' == inp[0]:
        break
    그램.append(list(map(int, inp))[1:])
for top in 그램:   
    스택 = []
    최대너비 = 0
    idx = 0
    for i in range(len(top)):
        인덱스 = idx
        if not 스택:
            스택.append((i, top[i]))
            idx += 1
            continue
        while 스택:
            if 스택[-1][1] > top[i]:
                뺀놈 = 스택.pop()
                최대너비 = max(최대너비, (i-뺀놈[0]) * 뺀놈[1])
                # 스택.append((뺀놈[0], top[i]))
                인덱스 = 뺀놈[0]
            elif 스택[-1][1] < top[i]:
                스택.append((인덱스, top[i]))
                break
            else :
                break
            if not 스택:
                스택.append((인덱스, top[i]))
        idx +=1
    남은너비 = 0
    for s in range(len(스택)):
        남은너비 = max(남은너비, (i-스택[s][0]+1)*스택[s][1])
    print(max(최대너비, 남은너비))
