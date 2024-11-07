import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)

def DFS(start):
    visited[start]=1
    for next_node in towns[start]:
        if not visited[next_node]:
            DFS(next_node)
            dp[start][1]+=dp[next_node][0]
            dp[start][0]+=max(dp[next_node][0], dp[next_node][1])
n=int(input())
town_peoples=[0]+list(map(int, input().split()))
dp=[[0, town_peoples[i]]*2 for i in range(n+1)]
visited=[0]*(n+1)
towns=[[]*(n+1) for _ in range(n+1)]

for _ in range(n-1):
    a,b=map(int, input().split())
    towns[a].append(b)
    towns[b].append(a)
DFS(1)
print(max(dp[1][0],dp[1][1]))