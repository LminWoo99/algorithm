import sys
import math
input=sys.stdin.readline
def find(x):
    if x!=connect[x]:
        connect[x]=find(connect[x])
    return connect[x]
def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        connect[b]=a
    else:
        connect[a]=b
n,m=map(int, input().split())
god=[]
connect=[i for i in range(n+1)]
for _ in range(n):
    x,y=map(int, input().split())
    god.append((x,y))
for _ in range(m):
    a,b=map(int, input().split())
    union(a,b)
edges=[]
for i in range(n-1):
    for j in range(i+1, n):
        x,y=god[i][0], god[i][1]
        x1, y1=god[j][0], god[j][1]
        dist=math.sqrt((x1-x)**2+(y1-y)**2)
        edges.append((i+1,j+1, dist))
edges.sort(key=lambda x: x[2])
res=0
for edge in edges:
    a,b,dist=edge[0], edge[1], edge[2]
    if find(a)!=find(b):
        union(a,b)
        res+=dist
print(f"{res:.2f}")