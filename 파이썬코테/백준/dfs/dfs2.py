from collections import deque
def DFS(v):
    visit1[v]=1
    print(v, end=' ')
    for i in range(1, n+1):
        if visit1[i]==0 and li[v][i]:
            DFS(i)
def BFS(v):
    dq=deque([v])
    visit2[v]=1
    while dq:
        v=dq.popleft()        
        print(v, end=' ')
        for i in range(1, n+1):
            if visit2[i]==0 and li[v][i]==1:
                dq.append(i)
                visit2[i]=1
n,m,v=map(int, input().split())
li=[[0 for i in range(n+1)] for j in range(n+1)]
visit1=[0]*(n+1)
visit2=[0]*(n+1)
for i in range(m):
    a, b=map(int, input().split())
    li[a][b]=1
    li[b][a]=1
DFS(v)
print()
BFS(v)
