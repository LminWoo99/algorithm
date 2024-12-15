import sys
input=sys.stdin.readline

t,w = map(int, input().split())
trees_info=[]
for _ in range(t):
    trees_info.append((int(input())))
# dp=[[0]*2 for _ in range(t+1)]
dp=[[0]*(w+1) for _ in range(t+1)]
for i in range(1, t+1):
    if trees_info[i-1]==1:
        dp[i][0]=dp[i-1][0]+1
    else:
        dp[i][0]=dp[i-1][0]
    for j in range(1, w+1): 
        ##  자두를 먹을 수 있는 조건
        if (trees_info[i-1]==1 and j%2==0) or (trees_info[i-1]==2 and j%2==1):
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-1])+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])
print(max(dp[-1]))