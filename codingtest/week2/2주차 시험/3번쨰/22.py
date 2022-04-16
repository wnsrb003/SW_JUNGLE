#요세푸스

import heapq
n, k = list(map(int, input().split()))
사람 = list(map(int, [i for i in range(1, n+1)]))
결과 = []

index = 1
while 사람:
    뺀놈 = 사람.pop(0)
    if index % k == 0:
        결과.append(str(뺀놈))
    else:
        사람.append(뺀놈)
    index += 1
print('<' + ', '.join(결과) + '>')