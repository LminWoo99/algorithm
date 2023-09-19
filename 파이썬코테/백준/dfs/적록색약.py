import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(x,y):
    visit[x][y]=True
    cur_color=a[x][y]
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and a[xx][yy]==cur_color and visit[xx][yy]==False:
            dfs(xx,yy)
    
n=int(input().rstrip())
dx=[-1, 0, 1, 0]
dy=[0, 1, 0 , -1]
visit=[[False]*n for _ in range(n)]
a=[list(map(str, input().rstrip())) for _ in range(n)]
cnt=0
red_cnt=0
for i in range(n):
    for j in range(n):
        if visit[i][j]==False:
            dfs(i,j)
            cnt+=1
for i in range(n):
    for j in range(n):
        if a[i][j]=='G':
            a[i][j]='R'
visit=[[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visit[i][j]==False:
            dfs(i,j)
            red_cnt+=1
print(cnt, red_cnt)