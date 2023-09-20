def DFS(L, s):
    global cnt
    if L==k:
        sum=0
        for i in range(k):
            sum+=res[i]
        if sum%m==0:
            cnt+=1
    else:
        for i in range(s, len(a)):
            res[L]=a[i]
            DFS(L+1, i+1)
    
n, k=map(int, input().split())
a=list(map(int, input().split()))
m=int(input())
res=[0]*k
cnt=0
DFS(0, 0)
print(cnt)