# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    maxLength = 0
    cnt = 1
    dic = []
    for i in range(len(S)):
        if (i == len(S)-1):
            dic.append(cnt)
            maxLength = max(maxLength, cnt)
        else:
            if (S[i] == S[i+1]):
                cnt += 1
            else:
                dic.append(cnt)
                maxLength = max(maxLength, cnt)
                cnt = 1
    result = 0
    while(dic):
        result += maxLength - dic.pop()
    return result
print(solution("aaabbbababab"))