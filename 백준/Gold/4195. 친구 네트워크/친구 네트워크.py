import sys
input=sys.stdin.readline
from collections import defaultdict
t=int(input())
def find(x):
    if x!=friend[x]:
        friend[x]=find(friend[x])
    return friend[x]
def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        friend[b]=a
        network[a]+=network[b]
    print(network[a])
for _ in range(t):
    f=int(input())
    network=defaultdict(int)
    friend=defaultdict(str)
    for i in range(f):
        a,b=input().rstrip().split()
        if not friend[a]:
            friend[a]=a
            network[a]=1
        if not friend[b]:
            friend[b]=b
            network[b]=1
        union(a,b)