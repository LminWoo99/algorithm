import sys
sys.setrecursionlimit(1000000)
def dfs(x,y):
    visit[x][y]=True
    for i in range(8):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<h and 0<=yy<w and visit[xx][yy]==False and a[xx][yy]==1:
            dfs(xx,yy)
            
    
dx=[-1, 0, 1, 0, 1,-1, -1, 1]
dy=[0, 1, 0 , -1,1, -1, 1, -1]
result=[]
while True:
    w, h=map(int, input().split())
    if w!=0 and h!=0:
        a=[list(map(int, input().split())) for _ in range(h)]
        visit=[[False]*w for _ in range(h)]
        cnt=0
        for i in range(h):
            for j in range(w):
                if visit[i][j]==False and a[i][j]==1:
                    dfs(i,j)
                    cnt+=1
        result.append(cnt)
    else:
        break
for i in result:
    print(i)