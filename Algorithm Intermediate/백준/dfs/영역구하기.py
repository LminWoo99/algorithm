import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline
def dfs(x,y):
    global cnt
    visit[x][y]=1
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<m and 0<=yy<n and visit[xx][yy]==0:
            cnt+=1
            dfs(xx,yy)
m,n,k=map(int, input().split())
visit=[[0]*n for _ in range(m)]
for _ in range(k):
    a,b,c,d=map(int, input().split())
    for i in range(b,d):
        for j in range(a,c):
            visit[i][j]=1
dx=[-1,0,1,0]
dy=[0,1,0,-1]
cnt=1
area=0
ans=[]
for i in range(m):
    for j in range(n):
        if visit[i][j]==0:
            area+=1
            dfs(i,j)
            ans.append(cnt)
            cnt=1
ans.sort()
print(area)
print(' '.join(map(str, ans)))