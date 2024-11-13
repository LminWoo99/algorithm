import sys
input=sys.stdin.readline
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    x=find(x)
    y=find(y)
    if x in a and y in a:
        return 
    if x in a:
        parent[y]=x
    elif y in a:
        parent[x]=y
    else:
        if x<y:
            parent[y]=x
        else:
            parent[x]=y

n,m=map(int , input().split())
a=list(map(int, input().split()))[1:] # 진실을 아는 사람
parent=list(range(n+1))
res=0
partys=[]
for _ in range(m):
    party=list(map(int, input().split()))
    party_len =party[0]
    party=party[1:]
    for i in range(party_len-1):
        union(party[i], party[i+1])
    partys.append(party)
for party in partys:
    flag=True
    for i in range(len(party)):
        if find(party[i]) in a:
            flag=False
            break
    if flag:
        res+=1
print(res)   