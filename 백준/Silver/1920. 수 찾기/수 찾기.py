import sys
input=sys.stdin.readline


n=int(input())
a=list(map(int, input().split()))
a.sort()
m=int(input())
b=list(map(int, input().split()))
for i in b:
    res=0
    target=i
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        if a[mid]==target:
            res=1
            break
        elif a[mid]>target:
            end=mid-1      
        else:
            start=mid+1
    print(res)
        