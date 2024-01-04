import sys
input=sys.stdin.readline
s=input().rstrip()
m=int(input())
a=[]
for _ in range(m):
    x,y=input().split()
    a.append((x,int(y)))
dp = [0] * (len(s) + 1)

for i in range(1, len(s) + 1):
    for j in range(m):
        length = len(a[j][0])
        if i >= length and s[i - length:i] == a[j][0]:
            dp[i] = max(dp[i], dp[i - length] + a[j][1])

    dp[i] = max(dp[i], dp[i - 1] + 1)
    
print(dp[-1])



