def DFS(L, s):
    global cnt
    if L==m:
        for i in range(m):
            print(a[i], end=' ')
        cnt+=1
        print()
    
    else:
        for i in range(s, n+1):
            a[L]=i
            DFS(L+1, i+1)            
n, m=map(int, input().split())
cnt=0
a=[0]*m
DFS(0, 1)
print(cnt)