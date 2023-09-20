import sys;
input=sys.stdin.readline
def DFS( L, total, x, y):
    global maximum
    if maximum>=total+max_val*(4-L):
        return
    if L==4:
        maximum=max(total, maximum)
        return
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<n and 0<=yy<m and visit[xx][yy]==0:
                if L==2:
                    visit[xx][yy]=1
                    DFS(L+1, total+a[xx][yy],  x, y)
                    visit[xx][yy]=0
                visit[xx][yy]=1
                DFS(L+1, total+a[xx][yy],  xx, yy)
                visit[xx][yy]=0
                
n,m =map(int, input().split())
a=[list(map(int, input().split())) for _ in range(n)]
visit=[([0]*m) for _ in range(n)]
maximum=0
max_val=max(map(max , a))
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
for i in range(n):
    for j in range(m):
        visit[i][j]=1
        DFS(1, a[i][j], i ,j)
        visit[i][j]=0
        
print(maximum)