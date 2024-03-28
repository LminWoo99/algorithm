import sys
sys.setrecursionlimit(1000000) # 재귀 깊이 제한 늘리기
input=sys.stdin.readline
def find(x):
    if a[x]!=x:
        a[x]=find(a[x])
    return a[x]
def union(x,y):
    x=find(x)
    y=find(y)
    if x<y:
        a[y]=x
    else:
        a[x]=y

n,m = map(int, input().split())
a=[i for i in range(0, n+1)]
for i in range(m):
    type,x,y=map(int,input().split())
    if type==0:
        union(x,y)
    else:
        if find(x)==find(y):
            print("YES")
        else:
            print("NO")
            

    
    
    
