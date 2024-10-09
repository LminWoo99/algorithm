import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline
def DFS(start):
    visit[start]=1
    if not len(graph[start]):
        dp[start][1]=1
        dp[start][0]=0
    else:
        for node in graph[start]:
            if not visit[node]:
                DFS(node)
                dp[start][1]+=min(dp[node][1], dp[node][0])
                dp[start][0]+=dp[node][1]
        dp[start][1]+=1

n=int(input())
graph=[[]*(n+1) for _ in range(n+1)]
dp=[[0,0] for _ in range(n+1)]

for _ in range(n-1):
    u,v=map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visit=[0]*(n+1)
DFS(1)
print(min(dp[1][0],dp[1][1]))