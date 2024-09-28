dx=[-1,0,1,0]
dy=[0,1,0,-1]

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def DFS(x,y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y]=1
    for i in range(4):
        xx,yy=x+dx[i], y+dy[i]
        if 0<=xx<n and 0<=yy<n and forest[x][y]<forest[xx][yy]:
            dp[x][y]=max(dp[x][y], DFS(xx,yy)+1)
    return dp[x][y]
        
n=int(input())
forest=[list(map(int, input().split())) for _ in range(n)]

dp=[[0]*n for _ in range(n)]

answer=0

for i in range(n):
    for j in range(n):
        answer=max(answer, DFS(i,j))
print(answer)