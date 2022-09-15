# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import defaultdict, deque

def solution(B):
    # write your code in Python 3.6
    xLength = len(B)
    yLength = len(B[0])
    aPosition = [-1, -1]

    for s in range(xLength):
        B[s] = list(B[s])

    for i in range(xLength):
        for j in range(yLength):
            if B[i][j] == 'A':
                aPosition = [i,j]
                continue
            elif B[i][j] == '.' or B[i][j] == 'X' or B[i][j] == '.X':
                continue
            elif B[i][j] == '>':
                y = j+1
                flag = True
                B[i][j] = 'X'
                while y < yLength and flag:
                    if B[i][y] == '.' or B[i][y] == '.X' : 
                        B[i][y] = '.X'
                        y += 1
                    elif B[i][y] == 'A':
                        return False
                    else:
                        flag = False
            elif B[i][j] == '<':
                y = j-1
                flag = True
                B[i][j] = 'X'
                while y >= 0 and flag:
                    if B[i][y] == '.' or B[i][y] == '.X': 
                        B[i][y] = '.X'
                        y -= 1
                    elif B[i][y] == 'A':
                        return False
                    else:
                        flag = False
            elif B[i][j] == 'v':
                x = i + 1
                flag = True
                B[i][j] = 'X'
                while x < xLength and flag:
                    if B[x][j] == '.' or B[x][j] == '.X': 
                        B[x][j] = '.X'
                        x += 1
                    elif B[x][j] == 'A':
                        return False
                    else:
                        flag = False
            elif B[i][j] == '^':
                x = i - 1
                flag = True
                B[i][j] = 'X'
                while x >= 0 and flag:
                    if B[x][j] == '.' or B[x][j] == '.X': 
                        B[x][j] = '.X'
                        x -= 1
                    elif B[x][j] == 'A':
                        return False
                    else:
                        flag = False
    

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q = deque()
    q.append(aPosition)
    B[aPosition[0]][aPosition[1]] = 'X'
    while(q):
        [x, y] = q.popleft()
        if (x == xLength -1 and y == yLength - 1):
            return True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < xLength and ny < yLength and B[nx][ny] != 'X' and B[nx][ny] != '.X':
                q.append([nx,ny])
                B[nx][ny] = 'X'
    return False

# print(solution(['X.....>', '..v..X.', '.>..X..', 'A......']))
print(solution(['...XA', '.X..^', '.XX..']))
# solution(['.v..', '...A', '....', '...^'])
