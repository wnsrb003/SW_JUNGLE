inp = int(input())
lis = []
for i in range(inp):
    lis.append(input())

for i in lis:
    cnt = list(i)
    score = 0
    for j in range(len(cnt)):
        if cnt[j] == 'O':
            for k in range(j, len(cnt)):
                if cnt[k] == 'X':
                    break
                else :
                    score += 1
    print(score)
            
