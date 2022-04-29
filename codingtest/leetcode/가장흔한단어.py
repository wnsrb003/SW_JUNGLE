class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import defaultdict
        arr = re.sub('[-=+,;#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\"\'·]', ' ', paragraph).split()
        graph = defaultdict(list)
        banned = list(map(lambda x: x.lower(), banned))
        for i in arr:
            i = i.lower()
            if not i in banned:
                if i in graph.keys():
                    graph[i] += 1
                else :
                    graph[i] = 1
        max = 0
        result = ''
        for i, v in graph.items():
            if v > max :
                max = v
                result = i
        return result