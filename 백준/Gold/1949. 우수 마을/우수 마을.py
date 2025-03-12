import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)
def DFS(cur_node):
    visited[cur_node]=1
    for next in trees[cur_node]:
        if not visited[next]:
            DFS(next)
            dp[cur_node][1]+=dp[next][0]
            dp[cur_node][0]+=max(dp[next][0], dp[next][1])
            
n=int(input())

towns=[0] + list(map(int, input().split()))
visited=[0]*(n+1)
trees=[[]*(n+1) for _ in range(n+1)]
dp=[[0, towns[i]] for i in range(n+1)]

for _ in range(n-1):
    x,y=map(int, input().split())
    trees[x].append(y)
    trees[y].append(x)

DFS(1)
print(max(dp[1][0],dp[1][1]))