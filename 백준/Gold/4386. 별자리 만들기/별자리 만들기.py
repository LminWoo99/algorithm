import math
import sys
sys.setrecursionlimit(1000000) # 재귀 깊이 제한 늘리기
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    x=find(x)
    y=find(y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y
n=int(input())
stars=[]
parent=[i for i in range (n+1)]

for _ in range(n):
    x,y=map(float, input().split())
    stars.append((x,y))
edges=[]
for i in range(n-1):
    for j in range(i+1, n):
        a_x, a_y=stars[i]
        b_x, b_y=stars[j]
        cost=math.sqrt((b_x-a_x)**2+(b_y-a_y)**2)
        edges.append((cost, i,j))
edges.sort()
res=0
for edge in edges:
    cost,a,b=edge
    if find(a)!=find(b):
        union(a, b)
        res+=cost
print(math.floor(res*100)/100)