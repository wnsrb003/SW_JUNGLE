import sys
sys.stdin = open('input.txt');
T = int(input())
N = [int(input()) for _ in range(T)]

def sum_num(nums):
    global result
    if sum(nums) == n:
        result += 1
        return
    if sum(nums) > n:
        return
    for i in [1,2,3]:
        nums.append(i)
        sum_num(nums)
        nums.pop()
for n in N:
    if n == 0:
        print(1)
        continue
    result = 0
    sum_num([])
    print(result)

    