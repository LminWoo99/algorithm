import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int, input().split()))


res=float("INF")
res_x,res_y=0,0
for i in range(n-1):
    cur=a[i]
    start,end = i+1, n-1
    while start<=end:
        mid=(start+end)//2
        tmp=cur+a[mid]
        if abs(tmp)<res:
            res=abs(tmp)
            res_x,res_y=cur,a[mid]
        if tmp<0:
            start=mid+1
        else:
            end=mid-1
print(res_x, res_y)
            