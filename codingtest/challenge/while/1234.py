from collections import defaultdict, deque
# def bfs(start):
#     q = deque()
#     q.append(start)
#     visited[start] = 1
#     while q:
#         pop = q.popleft()
#         for i in graph[pop]:
#             if not visited[i]:
#                 q.appendleft(i)
#                 visited[i] = 1
def solution(n, computers):
    graph = defaultdict(list)
    for i, c in enumerate(computers):
        for j, v in enumerate(c):
            if i == j:
                continue
            if v:
                graph[i+1].append(j+1)
    visited = [0 for _ in range(n+1)]
    answer = 0
    for i in range(1, len(visited)):
        if not visited[i]:
            q = deque()
            q.append(i)
            visited[i] = 1
            while q:
                pop = q.popleft()
                for j in graph[pop]:
                    if not visited[j]:
                        q.appendleft(j)
                        visited[j] = 1
            answer+=1
    print(answer)
    return answer

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	)