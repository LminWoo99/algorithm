import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input()) #동전의 가짓수
    coin=list(map(int, input().split()))
    m=int(input())
    dp=[0]*(m+1)
    dp[0]=1
    for target in coin:
        for i in range(1, m+1):
            if i>=target:
                dp[i]+=dp[i-target]
                
    print(dp[-1])