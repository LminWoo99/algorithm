def Count(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)
    return cnt
k, n=map(int, input().split())
temp=0
Line=[]
res=0
lag=0
for i in range(k):
    temp=int(input())
    Line.append(temp)
    lag=max(lag,temp)
lt=1
rt=lag
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
        
print(res)
    
    