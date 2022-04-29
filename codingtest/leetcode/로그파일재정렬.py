class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        from collections import deque
        num = []
        alp = []
        for i in logs:
            if i[-1].isdigit():
                num.append(i)
            else :
                alp.append(i)
        num.sort()
        alp.sort(key= lambda x: ([i for i in x.split()[1:]], x.split()[0]))
        return alp + num