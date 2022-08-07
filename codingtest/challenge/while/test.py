import sys

sys.stdin = open('input.txt')

s = input()

def reverse(s):
    if not len(s):
        return ''
    return reverse(s[1:]) + s[0]

print(reverse(s))