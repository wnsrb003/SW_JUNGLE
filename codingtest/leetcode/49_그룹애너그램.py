class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        sort_str = defaultdict(list)
        result = []
        for i,s in enumerate(strs):
            sort_str[''.join(sorted(list(s)))].append(strs[i])
        for i,v in sort_str.items():
           result.append(v)
        return result
        # return list(sort_str.values())