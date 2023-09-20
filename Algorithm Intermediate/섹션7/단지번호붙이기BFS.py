from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
n=int(input())
a=[list(map(int, input()))for _ in range(n)]
res=[]
cnt=0
q=deque()
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            a[i][j]=0
            q.append((i,j))
            cnt=1
            while q:
                tmp=q.popleft()
                for k in range(4):
                    xx=tmp[0]+dx[k]
                    yy=tmp[1]+dy[k]
                    if 0<=xx<n and 0<=yy<n and a[xx][yy]==1:
                        a[xx][yy]=0
                        q.append((xx,yy))
                        cnt+=1
            res.append(cnt)
print(len(res))
res.sort()
print(res)
for m in res:
    print(m)