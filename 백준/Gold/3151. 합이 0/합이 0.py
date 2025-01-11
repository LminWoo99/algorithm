import sys
from bisect import bisect_left

input=sys.stdin.readline

n=int(input())
a=list(map(int, input().split()))
a.sort()
res=0

for i in range(n-2):
    start=i+1
    end=n-1
    while start<end:
        if a[start]+a[end]+a[i]>0:
            end-=1
        else:
            if a[start]+a[end]+a[i]==0:
                if a[start]==a[end]:
                    res+=(end-start)
                else:
                    cnt=bisect_left(a, a[end])
                    res+=(end-cnt+1)
            start+=1
print(res)