import sys
input=sys.stdin.readline
from collections import defaultdict
m,n=map(int, input().split())
spaces=[]
for _ in range(m):
    spaces.append(list(map(int, input().split())))
for i in range(m):
    tmp=spaces[i][:]
    tmp.sort()
    order=defaultdict(int)
    for idx, val in enumerate(tmp):
        if not order[val]:
            order[val]=idx
    for j in range(n):
        spaces[i][j]=order[spaces[i][j]]

res=0
for i in range(m-1):
    for j in range(i+1, m):
        if spaces[i]==spaces[j]:
            res+=1
            
print(res)