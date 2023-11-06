import sys
input=sys.stdin.readline
n=int(input())

res=[]

for i in range(n):
    res.append((int(input()), i))
res=sorted(res)
ans=0
for i in range(n):
    ans=max(ans, res[i][1]-i)
print(ans+1)
                
    