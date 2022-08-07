import sys
sys.stdin = open('input.txt');

N, M = map(int, (input().split()))
graph = [[0 for _ in range(M+1)]for _ in range(N+1)]
def dfs(i, j):
    answer = 0
    if j > M:
        i, j = i+1, 1
    if i > N:
        return 0
    if graph[i-1][j] == 0 or graph[i][j-1] == 0 or graph[i-1][j-1] == 0:
        graph[i][j] = 1
        answer += (1 + dfs(i, j+1))
        graph[i][j] = 0
    answer += dfs(i, j+1)
 
    return answer
print(dfs(1,1)+1)