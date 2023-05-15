from collections import deque
n, m=map(int, input().split())
dq=deque()
degree=[0]*(n+1)
dis=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b=map(int, input().split())
    dis[a][b]=1
    degree[b]+=1
for i in range(1, n+1):
    if degree[i]==0:
        dq.append(i)
while dq:
    x=dq.popleft()
    print(x, end=' ')
    for i in range(1, n+1):
            if dis[x][i]==1:
                degree[i]-=1
                if degree[i]==0:
                    dq.append(i)
