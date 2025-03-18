import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int , input().split()))
k=int(input())

if sum(a)<=k:
    print(max(a))
else:
    left, right=1, max(a)
    while left<=right:
        mid=(left+right)//2
        total=0
        for i in a:
            if i>mid:
                total+=mid
            else:
                total+=i
        if total<=k:
            left=mid+1
        else:
            right=mid-1
    print(right)