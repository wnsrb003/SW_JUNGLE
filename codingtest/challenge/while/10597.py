import sys
sys.stdin = open('input.txt');
def dfs(index):
    if index == len(kr):
        print(*result)
        exit(0)

    if index +1 < len(kr):
        a = int(kr[index: index + 2])
        if a <= maxc and not visited[a]:
            visited[a] = 1
            result.append(a)
            dfs(index+2)
            result.pop()
            visited[a] = 0
    a = int(kr[index: index + 1])
    if not visited[a] and a != 0:
        visited[a] = 1
        result.append(a)
        dfs(index+1)
        result.pop()
        visited[a] = 0

kr = input()

if len(kr) < 10:
    print(*([i for i in kr]))
else:
    maxc = 9 + (len(kr) - 9) // 2
    visited = [0 for i in range(maxc+1)]
    result = []
    dfs(0)




