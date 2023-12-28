n=int(input()) 
s=[int(input()) for _ in range(n)] 
dp=[0]*(n) 
if len(s)<=2:
    print(sum(s))
else: # 계단이 3개 이상일 때
    dp[0]=s[0] # 첫째 계단 수동 계산
    dp[1]=s[0]+s[1] # 둘째 계단까지 수동 계산
    for i in range(2,n): # 3번째 계단 부터 dp 점화식 이용해서 최대값 구하기
        dp[i]=max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])
    print(dp[-1])