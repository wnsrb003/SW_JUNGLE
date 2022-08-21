def solution(record):
    answer = []
    from collections import deque
    chat = {"calls": []}
    for r in record:
        call = r.split(' ')[0]
        if call == 'Leave':
            call, id = r.split(' ')
            chat[id]['call'].appendleft(call)
            chat["calls"].append(id)
            continue
        call, id, name = r.split(' ')
        if chat.get(id):
            chat[id]['name'] = name
            chat[id]['call'].appendleft(call)
        else:
            chat[id] = {
                'name': name,
                'call': deque([])
            }
            chat[id]['call'].appendleft(call)
        chat["calls"].append(id)
    for c in chat["calls"]:
        call = chat[c]['call'].popleft()
        if call == "Leave":
            answer.append(f'{chat[c]["name"]}님이 나갔습니다.')
        elif call == "Enter":
            answer.append(f'{chat[c]["name"]}님이 들어왔습니다.')
    return answer

print(solution(["Enter a123 muzi", "Leave a123"]))