def dfs(v):
    global result
    visit[v]=1
    for i in range(1, n+1):
        if visit[i]==0 and a[v][i]==1:
            result+=1
            dfs(i)
n=int(input())
m=int(input())
a=[[0 for i in range(n+1)] for j in range(n+1)]
visit=[0]*(n+1)
result=0
for i in range(m):
    x,y=map(int, input().split())
    a[x][y]=1
    a[y][x]=1
dfs(1)
print(result)
