def DFS(L, sum):
    global res
    if L>n:
        return
    if L==n:
        if res<sum:
            res=sum
    else:
        DFS(L+pt[L], sum+p[L])
        DFS(L+1, sum)
n=int(input())
pt=list()
p=list()
for i in range(n):
    a,b=map(int, input().split())
    pt.append(a)
    p.append(b)
res=0
DFS(0,0)
print(res)
