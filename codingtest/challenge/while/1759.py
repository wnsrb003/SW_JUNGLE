import sys
sys.stdin = open('input.txt');
L, C = map(int, input().split());
pwd = list(input().split());

def find(king, visited):
    if len(king) == L:
        a = 0
        b = 0
        for i in king:
            if i in ['a', 'e', 'i', 'o', 'u']:
                a += 1
            else:
                b += 1
        if a >= 1 and b >= 2:
            result.append(''.join(king))
            return
    for i, p in enumerate(pwd):
        if not p in visited and king[-1] < p:
            king.append(p)
            visited.append(p)
            find(king, visited)
            visited.pop()
            king.pop()
    
result = []
for i, p in enumerate(pwd):
    find([p], [p])
print('\n'.join(result))