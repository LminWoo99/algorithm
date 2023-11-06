import sys
input=sys.stdin.readline

n,m =map(int, input().split())
a=list(map(int, input().split()))
start, end=1, max(a)
while start<=end:
    mid=(start+end)//2
    res=0
    for i in a:
        if i>mid:
            res+=i-mid
    if res>=m:
        start=mid+1
    else:
        end=mid-1
print(end)