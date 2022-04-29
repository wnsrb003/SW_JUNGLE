import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

def postOrder(preO, inO):
    if preO:
        root = preO[0]

        mid = inO.index(preO[0])  
    # mid = len(preO)
    
    # for i, v in enumerate(inOrder):
    #     if v == root:
    #         mid = i
    #         break
        postOrder(preO[1:mid+1], inO[:mid])
        postOrder(preO[mid+1:], inO[mid+1:])
        print(root, end=' ')
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline().strip())

    preOrder = [i for i in list(map(int, sys.stdin.readline().strip().split()))]
    inOrder = [i for i in list(map(int, sys.stdin.readline().strip().split()))]
    postOrder(preOrder, inOrder)
    print()


        



