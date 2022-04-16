import sys
from collections import defaultdict
sys.stdin = open('input.txt')
n = int(input())
dic = {}

for i in range(n):
    node, left, right = input().split()
    dic[node] = [left,right]

def preorder(dic, start):
    if start != '.': 
        print(start, end='')
        preorder(dic, dic[start][0])
        preorder(dic, dic[start][1])

def inorder(dic, start):
    if start != '.': 
        inorder(dic, dic[start][0])
        print(start, end='')
        inorder(dic, dic[start][1])

def postorder(dic, start):
    if start != '.': 
        postorder(dic, dic[start][0])
        postorder(dic, dic[start][1])
        print(start, end='')

preorder(dic, 'A')
print()
inorder(dic, 'A')
print()
postorder(dic, 'A')