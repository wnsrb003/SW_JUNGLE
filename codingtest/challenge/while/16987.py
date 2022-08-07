import sys
sys.stdin = open('input.txt')

n = int(input())
eggs = []
answer = 0
S, W = 0, 1
for _ in range(n):
    eggs.append(list(map(int, input().split())))

    def crash(nowIndex):
        global answer
        # 종료조건
        if nowIndex == n:
            breakEggs = 0 
            for i in range(n): 
                if eggs[i][S] <= 0:                
                    breakEggs += 1        
            answer = max(answer, breakEggs) 
            return

        if eggs[nowIndex][S] <= 0:        
            crash(nowIndex + 1)        
            return        

        isAllBroken = True    
        for targetIndex in range(n):        
            if targetIndex == nowIndex: 
                continue        
            if eggs[targetIndex][S] > 0:            
                isAllBroken = False            
                break    
        if isAllBroken:        
            answer = max(answer, n - 1)        
            return     

        for targetIndex in range(n):        
            if targetIndex == nowIndex: 
                continue        
            if eggs[targetIndex][S] <= 0: 
                continue        

            eggs[nowIndex][S] -= eggs[targetIndex][W]        
            eggs[targetIndex][S] -= eggs[nowIndex][W]        
            crash(nowIndex + 1)        

            eggs[nowIndex][S] += eggs[targetIndex][W]        
            eggs[targetIndex][S] += eggs[nowIndex][W]        
            
crash(0)
print(answer)