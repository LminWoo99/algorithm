from collections import deque
n,m=map(int, input().split())
a=[list(map(int,input().split()))for _ in range(m)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
dis=[[0]*n for _ in range(m)]

q=deque()
for i in range(m):
    for j in range(n):
        if a[i][j]==1:
            q.append((i,j))
while q:
    tmp=q.popleft()
    for k in range(4):
        x=tmp[0]+dx[k]
        y=tmp[1]+dy[k]
        if 0<=x<m and 0<=y<n and a[x][y]==0:
            a[x][y]=1
            dis[x][y]=dis[tmp[0]][tmp[1]]+1
            q.append(((x,y)))
flag=1
for i in range(m):
    for j in range(n):
        if a[i][j]==0:
            flag=0
result=0
if flag==1:
    for i in range(m):
        for j in range(n):  
            if dis[i][j]>result:
                result=dis[i][j]
    print(result)
else:
    print(-1)
        
    


