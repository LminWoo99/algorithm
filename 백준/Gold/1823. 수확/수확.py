import sys
input=sys.stdin.readline
sys.setrecursionlimit(2000)
n=int(input())
a=[int(input()) for _ in range(n)]
dp =[[0 for i in range(n)] for i in range(n)]

def DFS(s,e,cnt):
    if s==e:
        return a[s]*cnt
    if dp[s][e]:
        return dp[s][e]
    
    dp[s][e]=max(DFS(s+1,e,cnt+1)+cnt*a[s], DFS(s,e-1,cnt+1)+cnt*a[e])
    return dp[s][e]

print(DFS(0, n-1, 1))