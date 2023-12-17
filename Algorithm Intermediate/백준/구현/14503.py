import sys
input=sys.stdin.readline    
n ,m =map(int, input().split())
r,c,d=map(int, input().split())
robot=[list(map(int, input().split())) for _ in range(n)]
check=[[0]*m for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
cnt=1
check[r][c]=1
while True:
    flag=0
    for i in range(4):
        d=(d+3)%4
        xx=r+dx[d]
        yy=c+dy[d]
        if 0<=xx<n and 0<=yy<m and robot[xx][yy]==0 and check[xx][yy]==0:
            check[xx][yy]=1
            flag=1
            r,c=xx,yy
            cnt+=1
            break
    if flag==0:
        xx=r-dx[d]           
        yy=c-dy[d]
        if robot[xx][yy]!=1:
            r,c=xx,yy
        else:
            print(cnt)
            break
            
    
