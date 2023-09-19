n=int(input())
tmp=[]
dp=[0]*10000
for i in range(n):
    a=int(input())
    tmp.append(a)
dp[0]=tmp[0]
dp[1]=tmp[0]+tmp[1]
dp[2]=max(tmp[2]+tmp[0], tmp[2]+tmp[1], dp[1])
for j in range(3, n):
    dp[j]=max(dp[j-2]+tmp[j], dp[j-3]+tmp[j]+tmp[j-1], dp[j-1])
print(max(dp))
