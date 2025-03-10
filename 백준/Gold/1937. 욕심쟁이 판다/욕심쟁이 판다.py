import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
res=0
def DFS(x,y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y]=1
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and board[x][y]<board[xx][yy]:
            dp[x][y]=max(DFS(xx,yy)+1, dp[x][y])
    return dp[x][y]
dx=[-1,0,1,0]
dy=[0,1,0,-1]

n=int(input())
board=[list(map(int, input().split())) for _ in range(n)]
dp=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        res=max(res, DFS(i,j))
print(res)