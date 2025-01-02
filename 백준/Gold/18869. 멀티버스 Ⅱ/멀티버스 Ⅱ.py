import sys
input=sys.stdin.readline
from collections import defaultdict
m,n=map(int, input().split())
spaces=[]
for _ in range(m):
    spaces.append(list(map(int, input().split())))
res=defaultdict(int)
for i in range(m):
    tmp=spaces[i][:]
    tmp.sort()
    order=defaultdict(int)
    for idx, val in enumerate(tmp):
        if not order[val]:
            order[val]=idx
    for j in range(n):
        spaces[i][j]=order[spaces[i][j]]
    key=tuple(spaces[i])
    if not res[key]:
        res[key]=1
    else:
        res[key]+=1
result=0
for i in res.values():
    result+=(i*(i-1))//2
print(result)