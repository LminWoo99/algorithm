def DFS(L,sum, t):
    global res
    if t>m:
        return
    if L==n:
        if res<sum:
            res=sum
    else:
        DFS(L+1, sum+pv[L], t+pt[L])
        DFS(L+1, sum, t)
        
n, m=map(int, input().split())
pv=list()
pt=list()
for i in range(n):
    row, col=map(int, input().split())
    pv.append(row)
    pt.append(col)
res=0
DFS(0,0,0)
print(res)
# 조건이 시간이 m보다 넘으면 안되고 and sum이 이전 res보다 작