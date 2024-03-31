import sys
input=sys.stdin.readline
def find(x):
    if gate[x]<0:
        return x
    gate[x]=find(gate[x])
    return gate[x]
def union(r,x):
    r=find(r)
    x=find(x)
    if r==x:
        return
    gate[x]=r
g=int(input())
p=int(input())
gate=[-1 for i in range(g+1)]
res=0
for i in range(p):
    n=int(input())
    tmp=find(n)
    if tmp==0:
        break
    union(tmp-1, tmp)
    res+=1
    
print(res)