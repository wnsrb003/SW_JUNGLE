import sys
import heapq
sys.stdin = open('input.txt');

N = int(input())
q = []
for _ in range(N):
    nums = list(map(int, input().split()))
    if not q:
        for i in nums:
            heapq.heappush(q, i)
    else:
        for i in nums:
            if q[0] < i:
                heapq.heappush(q, i)
                heapq.heappop(q)

print(q[0])
# arr = [[i for i in list(map(int, input().split()))] for _ in range(N)]
# fo = [i for i in range(N)]
# def flat(arr):
#     result = []
#     for item in arr:
#         result += item
#     return result

# arr = flat(arr)
# arr.sort()
# print(arr[N * N - N])
