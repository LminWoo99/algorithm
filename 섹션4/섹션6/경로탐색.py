def DFS(L):
    global cnt
    if L==n:
        cnt+=1
    else:
        for i in range(1,n+1):
            if a[L][i]==1 and ch[i]==0:
                ch[i]=1
                DFS(i)
                ch[i]=0
        
n, m=map(int, input().split())
a=[[0 for j in range(n+1)] for i in range(n+1)]
ch=[0]*(n+1)
for i in range(m):
    row, col=map(int, input().split())
    a[row][col]=1
cnt=0
ch[1]=1
DFS(1)
print(cnt)