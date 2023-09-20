import sys
def DFS(L, sum):
    if L==n and sum==m:
        for x in p:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                DFS(L+1, sum+(a[L]*p[L]))
                ch[i]=0  
n, m=map(int, input().split())
ch=[0]*(n+1)
a=[1]*n
p=[0]*n
for i in range(1, n):
    a[i]=a[i-1]*(n-i)//i
DFS(0, 0)


