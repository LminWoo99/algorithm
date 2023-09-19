import sys
a=sys.stdin.readline().rstrip()
b=sys.stdin.readline().rstrip()
len1=len(a)
len2=len(b)
dp=[[0]*(len2+1) for _ in range(len1+1)]
for i in range(1, len1+1):
    for j in range(1, len2+1):
        if a[i-1]==b[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])
