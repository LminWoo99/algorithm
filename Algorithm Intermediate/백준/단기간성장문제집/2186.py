import sys
input=sys.stdin.readline
def DFS(x,y,L):
    if L==len(a):
        return 1
    if check[x][y][L] != -1:
        return check[x][y][L]
    check[x][y][L]=0
    for i in range(4):
        xx,yy=x,y
        for _ in range(k):
            nx,ny=xx+dx[i], yy+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny]==a[L]:
                    check[x][y][L]+=DFS(nx,ny,L+1)
            xx,yy=nx,ny
    return check[x][y][L]
n,m,k=map(int, input().split())
board=[list(input().rstrip()) for _ in range(n)]
a=list(input().rstrip())
dx=[-1,0,1,0]
dy=[0,1,0,-1]
res=0
cand=[]
for i in range(n):
    for j in range(m):
        if board[i][j]==a[0]:
            cand.append((i,j))
ans=0
check=[[[-1]*len(a) for _ in range(m)]for _ in range(n)]
for i in range(len(cand)):
    x,y=cand[i]
    ans+=DFS(x,y,1)
print(ans)