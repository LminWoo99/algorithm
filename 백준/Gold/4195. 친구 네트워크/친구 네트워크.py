import sys
from collections import defaultdict
sys.setrecursionlimit(1000000) # 재귀 깊이 제한 늘리기
input=sys.stdin.readline
def find(x):
    if x!=master[x]:
        master[x]=find(master[x])
    return master[x]
def union(x,y):
    x=find(x)
    y=find(y)
    if x!=y:
        master[y]=x
        network[x]+=network[y]
    res.append(network[x])
t=int(input())

res=[]
for _ in range(t):
    network=defaultdict(int)
    master=defaultdict(str)
    f=int(input())
    for _ in range(f):
        a,b=map(str, input().rstrip().split())
        if not master[a]:
            master[a]=a
            network[a]=1
        if not master[b]:
            master[b]=b
            network[b]=1
        union(a,b)
for i in res:
    print(i)