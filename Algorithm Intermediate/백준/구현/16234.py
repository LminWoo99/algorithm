import sys
input=sys.stdin.readline
from collections import deque
def solution(i,j,num,flag):
    global visit

    dq=deque()
    dq.append((i,j))
    
    while dq:
        i,j=dq.popleft()
        for k in range(4):
            ii , jj=dx[k]+i, dy[k]+j
            if 0<=ii<n and 0<=jj<n and visit[ii][jj]==0 and l<=abs(country[ii][jj]-country[i][j])<=r:
                flag=True
                visit[i][j]=num            
                visit[ii][jj]=num
                dq.append((ii,jj))
                    ## 지금문제가 떨어져있는 영역을 어떻게 구분할것 인가?
    return flag
def divide(visit):
    global cnt
    a=[[0]*2 for _ in range(2000)]
    tmp=1
    country_count=0
    for i in range(n):
        for j in range(n):
            if visit[i][j]!=0:
                a[visit[i][j]][0]+=country[i][j]
                a[visit[i][j]][1]+=1
    for i in range(n):
        for j in range(n):
            if visit[i][j]!=0:
                country[i][j]=a[visit[i][j]][0]//a[visit[i][j]][1]
    
    cnt+=1
n,l,r=map(int, input().split())
dx=[-1,0,1,0]
dy=[0,1,0,-1]
cnt=0
country=[list(map(int, input().split())) for _ in range(n)]

while True:
    flag=False
    num=1
    visit=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visit[i][j]==0:
                flag=solution(i,j,num,flag)
            if flag:
                num+=1
    
    if num==1:
        break           
    else:
        divide(visit)
print(cnt)
