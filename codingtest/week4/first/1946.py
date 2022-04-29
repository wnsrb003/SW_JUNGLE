import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    test = []
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().strip().split())
        
        test.append((x, y))
    
    cnt = 1
    test.sort()
    max_b = test[0][1]
    for j in range(1, len(test)):
        if test[j][1] < max_b:
            max_b = test[j][1]
            cnt += 1
    
    
    print(cnt)
    

# import sys

# answer = []
# for _ in range(int(sys.stdin.readline())):
#     n = int(sys.stdin.readline())
#     test = [0] * (n+1)
#     for _ in range(n):
#         paper, interview = map(int, sys.stdin.readline().split())
#         test[paper] = interview

#     max_test = test[1]
#     cnt = 1
#     for i in range(2, n+1):
#         if max_test > test[i]:
#             max_test = test[i]
#             cnt += 1
#     answer.append(cnt)

# for i in answer:
#     print(i)