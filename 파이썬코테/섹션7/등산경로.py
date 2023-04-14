def DFS(x,y):
    global res
    if x==n-1 and y==n-1:
        res+=1
    else:
        for b in range(4):
            xx=x+dx[b]
            yy=y+dy[b]
            if 0<xx<n and 0<yy<n and a[x][y]<a[xx][yy] and ch[xx][yy]==0:
                ch[xx][yy]==1
                DFS(xx, yy)
                ch[xx][yy]==0
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
ch=[[0]*n for _ in range(n)]
mi=1000
ma=0
res=0
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
for i in range(n):
    for j in range(n):
        if mi>a[i][j]:
            mi=a[i][j]
        if ma<a[i][j]:
            ma=a[i][j]
ch[0][0]=1
DFS(0,0)
print(res)

