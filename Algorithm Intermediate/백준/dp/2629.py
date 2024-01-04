import sys
input=sys.stdin.readline
from itertools import permutations

n=int(input())
weight=list(map(int, input().split()))
cnt=int(input())
bead=list(map(int, input().split()))


dp=[[0]*(30*500+1) for _ in range(n+1)]
result=set()
def cal(weight, n, now, left, right):
    cnt=abs(left-right)
    if cnt not in result:
        result.add(cnt)
    if now==n:
        return 0
    if dp[now][cnt]==0:
        dp[now][cnt]=1
        cal(weight, n, now+1, left+weight[now], right)
        cal(weight, n, now+1, left, right+weight[now])
        cal(weight, n, now+1, left, right)

        
cal(weight, n, 0,0,0)
res=[]
for i in bead:
    if i in result:
        res.append('Y')
    else:
        res.append('N')
print(*res)
    
            

        
        
    


