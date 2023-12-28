import sys
input=sys.stdin.readline

n=int(input())
dp=[0]*(n+1)
if n==1:
    print(1)
elif n==2:
    print(3)
else:    
    dp[1]=1
    dp[2]=3
    for i in range(3, n+1):
        dp[i]=2*dp[i-2]+dp[i-1]
    print(dp[-1]%10007)



# 3==5
# 4-> 9
# 5-> 17
# 6-> 31
# n-> 57