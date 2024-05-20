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
n,m=map(int, input().split())
house=[]
parent=[i for i in range(n+1)]

for _ in range(m):
    a,b,c =map(int, input().split())
    house.append((a,b,c))
house.sort(key=lambda x:x[2])
res=0
cnt=0
for a,b,c in house:
    if find(a)!=find(b):
        union(a,b)
        cnt=max(cnt, c)
        res+=c
print(res-cnt)
    

    