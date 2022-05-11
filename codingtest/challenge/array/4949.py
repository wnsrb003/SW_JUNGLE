# https://www.acmicpc.net/problem/4949
import sys
sys.stdin = open('input.txt')

while True:
    inp = sys.stdin.readline()
    if inp == '.':
        break
    # print(inp)
    stack = []
    flag = True
    for i in inp:
        if i == ')' or i == ']':
            if not stack:
                flag = False
                break
            pop = stack.pop()
            if i == ')' and pop != '(':
                flag = False
                break
            elif i == ']' and pop != '[': 
                flag = False
                break
        elif i == '(' or i == '[':
            stack.append(i)
    if stack or not flag:
        print('no')
    else:
        print('yes')