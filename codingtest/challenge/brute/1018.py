from collections import defaultdict
tickets = [["JFK","KUL"],["JFK","ART"],["NRT","JFK"]]
dic = defaultdict(list)
for a, b in sorted(tickets):
    dic[a].append(b)
result = []
# dfs('JFK')
stack = ['JFK']
while stack:
    while dic[stack[-1]]:
        stack.append(dic[stack[-1]].pop(0))
    result.append(stack.pop())
print(result[::-1])