import sys
input=sys.stdin.readline
def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y,idx):
    x=find(x)
    y=find(y)
    if x!=y:
        parent[max(x,y)]=min(x,y)
        return 0
    else:
        return idx
        
n,m=map(int, input().split())
parent=[i for i in range(n)]

for i in range(m):
    x,y=map(int, input().split())
    res=union(x,y, i+1)
    if res:
        break
print(res)