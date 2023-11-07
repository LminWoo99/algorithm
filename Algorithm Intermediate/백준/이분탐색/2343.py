import sys
input=sys.stdin.readline


n, m =map(int, input().split())
a=list(map(int, input().split()))    
start, end= 1,sum(a)
result=0

while start<=end:
    mid=(start+end)//2
    tmp=0
    res=1
    max_tmp=0
    for i in range(n):
        if tmp+a[i]<=mid:
            tmp+=a[i]
        elif a[i]>mid:
            res=10000
            break
        else:
            res+=1
            tmp=a[i]

    if res>m:
        start=mid+1
        
    else:
        end=mid-1
        result=mid

    
print(result)
            
    