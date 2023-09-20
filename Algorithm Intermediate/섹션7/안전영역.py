import sys 
sys.setrecursionlimit(10**5)
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def DFS(qq,x,y):
    ch[x][y]=0
    for k in range(4):
        xx=x+dx[k]
        yy=y+dy[k]
        if 0<=xx<n and 0<=yy<n and a[xx][yy]>qq and ch[xx][yy]==1:
            DFS(qq, xx, yy)
n=int(input())
a=[list(map(int, input().split()))for _ in range(n)]
res=0
cnt=0
h=0
for i in range(n):
    for j in range(n):
        if h<a[i][j]:
            h=a[i][j]
for q in range(h):
    ch=[[1]*n for _ in range(n)]
    cnt=0
    for i in range(n):
        for j in range(n):
            if ch[i][j]==1 and a[i][j]>q:
                cnt+=1
                DFS(q,i,j)
    res=max(res,cnt)       
print(res)