import sys
input=sys.stdin.readline
def getDepth(x):
    return (x-2)//k+1
n,k,q=map(int, input().split())
def lcs(x,y):
    res=0
    while x!=y:
        if x>y:
            x=getDepth(x)
        else:
            y=getDepth(y)
        res+=1
    return res
for _ in range(q):
    x,y=map(int, input().split())
    if k==1:
        print(abs(x-y))
        continue
    print(lcs(x,y))