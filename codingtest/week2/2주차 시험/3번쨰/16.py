n = input()
스택 = []
점수 = 1
결과 = 0
for i in range(len(n)):
    if n[i] == '(':
        점수 *= 2
        스택.append('(')
    elif n[i] == '[':
        점수 *= 3
        스택.append('[')
    elif n[i] == ')':
        if not 스택 or 스택[-1] == '[':
            결과 = 0
            break
        if n[i-1] == '(':
            결과 += 점수
        점수 = 점수 // 2
        스택.pop()
    else :
        if not 스택 or 스택[-1] == '(':
            결과 = 0
            break
        if n[i-1] == '[':
            결과 += 점수
        점수 = 점수 // 3
        스택.pop()
if 스택:
    결과 = 0
print(결과) 
    