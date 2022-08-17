def solution(order):
    from collections import deque
    queue = deque([i for i in range(1, len(order)+1)])
    stack = []
    answer = []
    for i in order:
        if stack and stack[-1] == i:
            answer.append(stack.pop())
            continue
        while queue:
            q = queue.popleft()
            if q == i:
                answer.append(q)
                break
            stack.append(q)
        else:
            break
    return len(answer)

print(solution([5,4,3,2,1]))