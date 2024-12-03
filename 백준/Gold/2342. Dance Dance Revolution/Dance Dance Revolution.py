import sys
input=sys.stdin.readline
def calculate(x,y):
    if x==0:
        return 2
    elif x==y:
        return 1
    elif abs(x-y)==2:
        return 4
    else:
        return 3
    
a=list(map(int, input().split()))
dp=[[[4*len(a) for _ in range(5)]for _ in range(5)]for _ in range(len(a))]
dp[0][0][0]=0
for i in range(len(dp)-1):
    tmp=a[i]
    for left in range(5):
        for right in range(5):
            dp[i+1][left][tmp]=min(dp[i+1][left][tmp], dp[i][left][right]+calculate(right, tmp))
            dp[i+1][tmp][right]=min(dp[i+1][tmp][right], dp[i][left][right]+calculate(left, tmp))
print(min(map(min, dp[-1])))