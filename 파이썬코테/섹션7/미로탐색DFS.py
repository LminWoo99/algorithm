def DFS(x,y):
    global res
    if x==6 and y==6:
        res+=1
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<=6 and 0<=yy<=6 and a[xx][yy]==0:
                a[xx][yy]=1
                DFS(xx, yy)
                a[xx][yy]=0
    
a=[list(map(int, input().split()))for _ in range(7)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
a[0][0]=1
res=0
DFS(0,0)
print(res)
