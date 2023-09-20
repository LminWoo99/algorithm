import sys
def DFS(L,sum):
    global tmp
    if sum>T:
        return
    if L==p:
       if sum==T:
           tmp+=1    
    else:
        for i in range(b[L]+1):
            DFS(L+1, sum+(a[L]*i))
T=int(input())
p=int(input())
a=list()
b=list()
for i in range(p):
    res, res1=map(int, input().split())
    a.append(res)
    b.append(res1)
tmp=0
DFS(0,0)
print(tmp)

    