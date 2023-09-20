n = int(input())
dp = []

for i in range(n) :                            ## 입력값 이차원리스트 형태로 dp테이블에 저장하기
    dp.append(list(map(int,input().split())))
for i in range(1,n):
    for j in range(0,i+1):
        if j==0:
            dp[i][0]+=dp[i-1][0]
        elif j==i:
            dp[i][j]+=dp[i-1][j-1]
        else:
            dp[i][j]+=max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[n-1]))