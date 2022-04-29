# 마이너스를 만나면 다음 마이너스까지 싹다 더하고 -> split -


import sys
sys.stdin = open('input.txt')

minus = list(input().split('-'))
# cnt = eval(minus[0])
cnt = 0
for i in minus[0].split('+'):
    cnt += int(i)

for i in range(1, len(minus)):
    # cnt -= eval(minus[i])
    temp = 0
    for j in minus[i].split('+'):
        temp += int(j)
    cnt -= temp
print(cnt)