import sys
n, k = list(map(int, sys.stdin.readline().strip().split()))
num = list(sys.stdin.readline().strip())
스택 = []
cnt = 0
index = 0
# while cnt < n-k:
#     for m in range(index, len(num)):
#         if len(스택) == cnt:
#             스택.append(num[m])
#             index = m+1
#             continue
#         if n-k <= n-m+cnt:
#             if 스택[cnt] < num[m]:
#                 스택.pop()
#                 스택.append(num[m])
#                 index = m+1
#         else :
#             break
#     cnt +=1

삭제 = k
for m in range(n):
    while 삭제 > 0 and 스택:
        if 스택[-1] < num[m]:
            스택.pop()
            삭제 -= 1
        else :
            break
    스택.append(num[m]) 

# print(int(''.join(스택)))
for i in range(n-k):
    print(스택[i],end="")