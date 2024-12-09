import sys
input=sys.stdin.readline
def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    x=find(x)
    y=find(y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y
n,m,k=map(int, input().split())
candy=[0]+list(map(int, input().split()))
graph=[[]*(n+1) for _ in range(n+1)]
parent=[i for i in range(n+1)]
cur_friend=[1]*(n+1)

dp=[0]*k
for _ in range(m):
    x,y=map(int, input().split())
    union(x,y)
for i in range(1, n+1):
    if i!=parent[i]:
        root=find(i)
        candy[root]+=candy[i]
        cur_friend[root]+=cur_friend[i]
for i in range(1, n+1):
    if i!=parent[i]:
        continue
    for j in range(k-1, cur_friend[i]-1, -1):
        dp[j]=max(dp[j], dp[j-cur_friend[i]]+candy[i])
print(max(dp))