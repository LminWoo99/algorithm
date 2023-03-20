def DFS(L):
    global res
    global money
    if L==n:
        cha=max(money)-min(money)
        if cha<res:
            tmp=set()
            for x in money:
                tmp.add(x)
            if len(tmp)==3:
                res=cha
    else:
        for i in range(3):
            money[i]+=a[L]
            DFS(L+1)
            money[i]-=a[L]
n=int(input())
a=list()
money=[0]*3
res=2147000
for i in range(n):
    tmp=int(input())
    a.append(tmp)
DFS(0)
print(res)