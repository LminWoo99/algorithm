import sys
input=sys.stdin.readline
from collections import deque
import copy
def rotate_circle(x, dist, k):
    for i in range(n):
        if (i+1)%x==0:
            for _ in range(k):
                dq=deque(circle[i])
                if dist%2==0:
                    dq.rotate(1)
                else:
                    dq.rotate(-1)
                dq=list(dq)
                circle[i]=dq
def remove():
    global avg_cnt
    tmp=copy.deepcopy(circle)
    judge=False
    for i in range(n):
        for j in range(m):
            flag=False
            for k in range(4):
                x,y=i+dx[k], j+dy[k]
                if 0<=x<n and 0<=y<m:
                    if tmp[i][j]!=0 and tmp[i][j]==tmp[x][y]:
                        flag=True
                        circle[x][y]=0
                elif 0<=x<n and (y==-1 or y==m):
                    if y==-1:
                        y=m-1
                    else:
                        y=0
                    if tmp[i][j]!=0 and tmp[i][j]==tmp[x][y]:
                        flag=True
                        circle[x][y]=0
            if flag:
                judge=True
                avg_cnt+=1
                circle[i][j]=0
    if not judge:
        avg(avg_cnt)
def avg(avg_cnt):
    cnt=0
    total=0
    for i in range(n):
        for j in range(m):
            if circle[i][j]!=0:
                cnt+=1
                total+=circle[i][j]
    if cnt!=0:
        avg_circle=(total/cnt)
        for i in range(n):
            for j in range(m):
                if circle[i][j]!=0:
                    if circle[i][j]>avg_circle:
                        circle[i][j]-=1
                    elif circle[i][j]<avg_circle:
                        circle[i][j]+=1
    
n,m,t=map(int, input().split())
dx=[-1,0,1,0]
dy=[0,1,0,-1]
circle=[list(map(int, input().split())) for _ in range(n)]
rotate=[list(map(int, input().split())) for _ in range(t)]
cnt=0
avg_cnt=0
while True:
    if cnt==t:
        break
    x,d,k=rotate[cnt]
    rotate_circle(x,d,k)
    remove()
    cnt+=1
print(sum(map(sum, circle)))

