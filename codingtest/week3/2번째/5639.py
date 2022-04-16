import sys
sys.stdin = open('input.txt')

array = []
while True:
    try:
        array.append(int(input()))
    except:
        break

def division(start, end):
    if start > end:
        return
    else :
        mid = end + 1
        for i in range(start+1, end+1):
            if array[start] < array[i]:
                mid = i
                break
        division(start+1, mid-1)
        division(mid, end)
        print(array[start])

division(0, len(array)-1)