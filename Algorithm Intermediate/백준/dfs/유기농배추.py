from collections import deque

def bfs(x,y):
    dq=deque()    
    dq.append((x,y))
    a[x][y]=0
    while dq:
        l,k=dq.popleft()
        for i in range(4):
            xx=l+dx[i]
            yy=k+dy[i]
            if 0<=xx<n and 0<=yy<m and a[xx][yy]==1:
                dq.append((xx,yy))
                a[xx][yy]=0
            
dx=[-1,0,1,0]
dy=[0, 1, 0, -1]
t=int(input())
for i in range(t):
    m,n,k=map(int, input().split())
    a=[[0]*(m) for _ in range(n)]
    cnt=0
    for j in range(k):
        x,y=map(int, input().split())
        a[y][x]=1
    for q in range(n):
        for w in range(m):
            if a[q][w]==1:
                bfs(q,w)
                cnt+=1
    print(cnt)
                