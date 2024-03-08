import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int, input().split()))
res=float("INF")
x,y=0,0
for i in range(n-1):
    cur=a[i]
    start=i+1
    end=n-1
    while start<=end:
        mid=(start+end)//2
        tmp=cur+a[mid]
        if abs(tmp)<res:
            res=abs(tmp)
            x,y=i, mid
            if tmp==0:
                break
        if  tmp<0:
            start=mid+1
            
        else:
            end=mid-1
print(a[x],a[y])
