import sys
input=sys.stdin.readline
from collections import deque
def BFS(n,k):
    tmp=0
    dq=deque()
    visit=[0]*100000
    visit[n]=1
    dq.append((n, tmp))
    while dq:
        x,tmp=dq.popleft()
        if x==k:
            break
        for i in range(3):
            if i==0 and visit[x*2]!=1:
                visit[x*2]=1
                dq.append((x*2, tmp+1))
            elif i==1  and visit[x+1]!=1:
                visit[x+1]=1
                dq.append((x+1, tmp+1))
            elif i==2 and visit[x-1]!=1:
                visit[x-1]=1
                dq.append((x-1, tmp+1))
    return tmp,visit
n,k=map(int, input().split())
res,res_path=BFS(n,k)
print(res)
for i in range(1,100000):
    if res_path[i]!=0:
        print(i, end=' ')
