#카드정렬하기
#https://www.acmicpc.net/problem/1715

import heapq
카드 = []
결과 = 0
n = int(input())
for i in range(n):
    inp = int(input())
    heapq.heappush(카드, inp)

while len(카드) > 1 :
    a = heapq.heappop(카드)
    b = heapq.heappop(카드)
    heapq.heappush(카드, a+b)
    결과 += a+b
print(결과)

