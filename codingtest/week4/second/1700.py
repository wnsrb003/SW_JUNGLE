import sys

sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

cnt = 0
con = []
for i in range(len(arr)):
    if arr[i] in con:
        continue
    elif len(con) < N:
        con.append(arr[i])
    else:
        flags = False
        max_index = temp = 0
        for j in range(len(con)):
            if not con[j] in arr[i+1:]:
                temp = j
                flags = True
                break
            elif arr[i+1::].index(con[j]) > max_index:
                max_index = arr[i+1::].index(con[j])
                temp = j

        # print(temp)
        con.pop(temp)
        cnt += 1
        con.append(arr[i])
print(cnt)

