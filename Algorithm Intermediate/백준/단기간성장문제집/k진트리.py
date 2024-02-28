import sys
input = sys.stdin.readline
def getParent(node):
    return (node-2)//k + 1
def lca(x,y):
    d = 0
    while x != y:
        if x > y:
            x = getParent(x)
        else:
            y = getParent(y)
        d += 1
    return d
n,k,q = map(int,input().split())
for _ in range(q):
    x,y = map(int,input().split())
    if k == 1:
        print(abs(x-y))
        continue
    print(lca(x,y))