import sys
import math
n,s=map(int, sys.stdin.readline().split())
a=list(map(int, sys.stdin.readline().split()))
i=0
temp=[]
for i in range(n):
    temp.append(abs(a[i]-s))
tmp=0
ans=temp[0]
for j in range(1,n):
    ans=math.gcd(ans, temp[j])
print(ans)

        
    