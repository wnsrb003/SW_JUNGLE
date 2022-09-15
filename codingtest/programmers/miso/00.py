# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A = list(set(A))
    A.sort(reverse = True)
    index = 1
    while index == A.pop():
        index += 1
    return index

print(solution([1,3,6,4,1,2]))