def solution(X, Y):
    from collections import defaultdict 
    answer = ''
    dicX = defaultdict(int)
    # dicY = defaultdict(int)
    _X, _Y = str(X), str(Y)
    for x in _X:
        dicX[x] += 1
    # for y in _Y:
    #     dicY[y] += 1
    pairs = []
    for y in _Y:
        if dicX[y]:
            pairs.append(y)
            dicX[y] -= 1
    if not len(pairs):
        return -1
    pairs.sort(reverse=True)
    if not int(pairs[0]):
        return 0

    return "".join(pairs)
    

    # return answer

print(solution(100, 33003))