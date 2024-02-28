# 크루스칼 알고리즘
import sys
input=sys.stdin.readline
v,e=map(int, input().split())
edges=[]
for _ in range(e):    
    edges.append(list(map(int, input().split())))
root=dict()
for i in range(1, v+1):
    root[i]=i
def find(x):
    if root[x]==x:
        return x
    else:
        root[x]=find(root[x])
        return root[x]
def union(x,y):
    x=root[x]
    y=root[y]
    root[y]=x
edges.sort(key=lambda x: x[2])
answer=0
for edge in edges:
    # 사이클이 만들어지는 edge라면 pass
    if find(edge[0])==find(edge[1]):
        continue
    else:
        union(edge[0], edge[1])
        answer+=edge[2]
print(answer)