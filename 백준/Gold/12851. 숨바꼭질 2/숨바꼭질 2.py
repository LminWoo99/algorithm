import sys
input=sys.stdin.readline
from collections import deque

n,k=map(int , input().split())
dq=deque()
dq.append((n,0))
visit=[0]*100001
visit[n]=1
ans=0
res=int(1e9)
while dq:
    cur, cnt=dq.popleft()
    if cur==k:
        ans+=1
        res=cnt
    if cnt>res:
        break
    for i in (cur-1 , cur+1, cur*2):
        if 0<=i<=100000 and (not visit[i] or visit[i]==cnt+1):
            visit[i]=cnt+1
            dq.append((i, cnt+1))
print(res)        
print(ans)