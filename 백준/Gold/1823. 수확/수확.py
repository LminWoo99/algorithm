import sys
input=sys.stdin.readline
sys.setrecursionlimit(2000)

n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))
dp=[[0 for _ in range(n)] for _ in range(n)]

def DFS(left, right, cnt):
    if left==right:
        return  a[left]*cnt
    if dp[left][right]:
        return dp[left][right]
    dp[left][right]=max(DFS(left+1, right, cnt+1)+cnt*a[left], DFS(left, right-1, cnt+1)+cnt*a[right])
    return dp[left][right]
print(DFS(0, n-1, 1))