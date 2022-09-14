# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    twoNum = format(N, 'b')
    print(twoNum)
    left = 0
    right = len(twoNum) - 1
    stack = []
    rightStack = []
    while(left <= right):
        if (twoNum[left] == '1'):
            stack.append(left)
        if (twoNum[right] == '1'):
            stack.append(right)
        left += 1
        right -= 1
    stack.sort()
    maxLen = 0
    start = stack.pop()
    while(stack):
        pop = stack.pop()
        maxLen = max(maxLen, start - pop - 1)
        start = pop
    print(maxLen)
#100001001000000
solution(15)