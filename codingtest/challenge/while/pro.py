from collections import defaultdict
def solution(clothes):
    answer = 1
    dic = defaultdict(list)
    for i in clothes:
        dic[i[1]].append(i[0])
    for i in dic.values():
        answer *= len(i)
    return (answer-1)