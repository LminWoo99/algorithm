import sys
input=sys.stdin.readline
import math
INF = float(1e9)
def calculate_distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2),2)
def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]
def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
n=int(input())
star=[]
for _ in range(n):
    x,y=map(float, input().split())
    star.append((x,y))
parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i
graph=[]
for i in range(n-1):
    for j in range(i+1,n):
        tmp=calculate_distance(star[i][0],star[i][1],star[j][0],star[j][1])
        graph.append((tmp, i,j))
graph.sort()
res=0
for a in graph:
    if find(a[1])!=find(a[2]):
        union(a[1],a[2])
        res+=a[0]
print(res)