import sys
input=sys.stdin.readline

n=int(input())
board= list(map(int, input().split()))
dp=[[0]*(n) for i in range(n)]

for i in range(n):
    dp[i][i]=1
for i in range(n-1):
    if board[i]==board[i+1]:
        dp[i][i+1]=1
    else:
        dp[i][i+1]=0
for i in range(n-2):
    for j in range(n-2-i):
        tmp=j+2+i
        if board[j]==board[tmp] and dp[j+1][tmp-1]==1:
            dp[j][tmp]=1
            

t=int(input())
for i in range(t):
    s,e=map(int, input().split())
    print(dp[s-1][e-1])


    