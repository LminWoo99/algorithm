from collections import deque
dx=[-1,0,1,0,-1,-1,1,1]
dy=[0,1,0,-1,-1,1,-1,1]
n=int(input())
a=[list(map(int, input().split()))for _ in range(n)]
q=deque()
cnt=0
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            a[i][j]=0
            q.append((i,j))
            cnt+=1
            while q:
                tmp=q.popleft()
                for m in range(8):
                    x=dx[m]+tmp[0]
                    y=dy[m]+tmp[1]
                    if 0<=x<n and 0<=y<n and a[x][y]==1:
                        a[x][y]=0
                        q.append((x,y))
print(cnt)


        
