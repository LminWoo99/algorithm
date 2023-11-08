import sys
input=sys.stdin.readline
def isValid(mid):
    global res
    max_x, max_y= a[0], a[0]
    cnt=1
    for i in range(1,n):
        max_x=max(max_x, a[i])
        max_y=min(max_y, a[i])
        if max_x-max_y> mid:
            cnt+=1
            max_x=a[i]
            max_y=a[i]
    return cnt
            
n,m =map(int, input().split())
a=list(map(int, input().split()))
start , end=0, max(a)
res=0
while start<=end:
    mid=(start+end)//2
    if isValid(mid)<=m:
        end=mid-1
        result=mid
    else:
        start=mid+1
print(result)
        