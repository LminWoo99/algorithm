def DFS(x,y):
    global res
    if dy[x][y]>0:
        return dy[x][y]
    if x==0 and y==0:
        return a[0][0]
    else:
        if y==0:
            dy[x][y]=DFS(x-1, y)+a[x][y]
        elif x==0:
            dy[x][y]=DFS(x, y-1)+a[x][y]
        else:
            dy[x][y]=min(DFS(x-1, y), DFS(x, y-1))+a[x][y]
        return dy[x][y]

n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
res=0
dy=[[0]*n for _ in range(n)]
print(DFS(n-1,n-1))

