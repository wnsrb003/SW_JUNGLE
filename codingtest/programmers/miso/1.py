# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    for i in range(len(A)-1, -1, -1):
        if (A[i] == A[i-1]): A.pop(i)
    if len(A) == 2:
        return 1
    answer = 0
    castles = []
    for i in range(len(A)-2, 0, -1):
        # 봉우리
        if (A[i-1] < A[i] and A[i+1] < A[i]):
            answer += 1
            castles.append(i)
        # 계곡
        if (A[i-1] > A[i] and A[i+1] > A[i]):
            answer += 1
            castles.append(i)
    if 1 not in castles: answer += 1
    if len(A) - 1 not in castles: answer += 1
    print(answer)
    return answer
# solution([2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5])
solution([-3, -3])
# def solution(A):
#     for i in range(len(A)-1, 0, -1):
#         if A[i] == A[i-1]:
#             A.pop(i)
#         else:
#             pass
#     a = 0
#     if len(A) == 1:
#         return 1
#     else:
#         for i in range(len(A)-1, 0, -1):
#             if A[i] < A[i-1] and A[i-2] < A[i-1]:
#                 a += 1
#             else:
#                 pass
#         if A[0] > A[1]:
#             a += 1
#         if A[-1] > A[-2]:
#             a += 1
#     for i in range(len(A)-1, 1, -1):
#         if A[i] > A[i-1] and A[i-2] > A[i-1]:
#             a += 1
#         else:
#             pass
#     if A[0] < A[1]:
#         a += 1
#     if A[-1] < A[-2]:
#         a += 1
#     return a

