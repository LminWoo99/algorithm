def dfs(x,y):
    global cnt
    cnt+=1
    a[x][y]=0
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and a[xx][yy]==1:
            dfs(xx, yy)
    
dx=[-1, 0, 1, 0]
dy=[0, 1, 0 , -1]
n=int(input())
tmp=[]

a=[list(map(int, input()))for _ in range(n)]
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            cnt=0
            dfs(i,j)
            tmp.append(cnt)
tmp.sort()
print(len(tmp))
for i in tmp:
    print(i)