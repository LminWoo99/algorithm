import sys
input=sys.stdin.readline
def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    x=find(x)
    y=find(y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y
v,e=map(int, input().split())
trees=[]
for _ in range(e):
    trees.append(list(map(int, input().split())))
parent=[0]*(v+1)
for i in range(1, v+1):
    parent[i]=i
trees.sort(key=lambda a:a[2])
res=0
for tree in trees:
    a,b,c=tree[0], tree[1], tree[2]
    if find(a)!=find(b):
        union(a,b)
        res+=c
print(res)