import sys
input=sys.stdin.readline
from collections import deque
import itertools
def check(visit):
    maxVirus=0
    cnt=0
    for i in range(n):
        for j in range(n):
            if visit[i][j]==0:
                cnt+=1
            maxVirus=max(maxVirus, visit[i][j])
    if cnt-m==temp:
        return maxVirus 
    else:
        return -1
            
def BFS(dq):
    dq=deque(dq)
    
    visit=[[0]*n for _ in range(n)]
    wow=[]
    for i in  range(m):
        wow.append(dq[i])
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<n and 0<=yy<n and visit[xx][yy]==0 and virus[xx][yy]!=1 and (xx,yy) not in wow:
                visit[xx][yy]=visit[x][y]+1
                dq.append((xx,yy))
    
    res=check(visit)
    return res
n,m =map(int, input().split())
virus=[list(map(int, input().split())) for _ in range(n)]


dx=[-1,0,1,0]
dy=[0,1,0,-1]
time=10000
test=[]
temp=0
for i in range(n):
    for j in range(n):
        if virus[i][j]==2:
            test.append((i,j))
        elif virus[i][j]==1:
            temp+=1
pr=itertools.combinations(test, m)
pr=list(pr)
for i in range(len(pr)):
    tmp=BFS(pr[i])
    if tmp!=-1:
        time=min(time, tmp)
if time==10000:
    print(-1)
else:
    print(time)
    