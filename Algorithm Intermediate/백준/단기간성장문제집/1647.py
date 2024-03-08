import sys
input=sys.stdin.readline
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
        
n,m=map(int, input().split())
graph=[]
parent = list(range(n + 1))
for i in range(m):
    a,b,c=map(int,input().split())
    graph.append((a,b,c))
graph.sort(key=lambda x:x[2])
last=0
answer=0
for a,b,c in graph:
    if find(a)!=find(b):
        union(a,b)
        answer+=c
        last=c
print(answer-last)