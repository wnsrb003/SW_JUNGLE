def solution(want, number, discount):
    answer = 0
    from collections import Counter

    for i in range(len(discount) - 9):
        cntDis = Counter(discount[i:i+10])
        flag = True
        for j in range(len(want)):
            if cntDis[want[j]] < number[j]:
                flag = False
                break
        if flag:
            answer += 1

    return answer