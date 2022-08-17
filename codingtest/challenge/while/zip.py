def solution(s):
    answer = 1000
    for i in range(1, len(s)//2 + 1):
        tmp = s[:i]
        cnt = 1
        res = ''
        for j in range(i, len(s)+i, i):
            # print(s[j:j+i])
            if tmp == s[j:j+i]: 
                cnt +=1
            else:
                if cnt == 1 : 
                    res += tmp
                else:
                    res += str(cnt) + tmp
                tmp = s[j:j+i]
                cnt = 1
        answer = min(len(res), answer)
    return answer
print(solution("abcabcabcabcdededededede"	))