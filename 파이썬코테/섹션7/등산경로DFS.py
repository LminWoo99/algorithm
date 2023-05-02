def DFS(x,y):
    
    global res
    if a[x][y]==temp:
        res+=1
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<=n-1 and 0<=yy<=n-1 and a[x][y]<a[xx][yy]:
                DFS(xx,yy)
                   
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
temp=0
tempMin=10000
tmp=[0,0]
res=0
for i in range(len(a)):
    for j in range(len(a)):
        if temp<a[i][j]:
            temp=a[i][j]
        if tempMin>a[i][j]:
            tempMin=a[i][j]
            tmp[0]=i
            tmp[1]=j
print(tmp[0], tmp[1])
DFS(tmp[0],tmp[1])
print(res)
