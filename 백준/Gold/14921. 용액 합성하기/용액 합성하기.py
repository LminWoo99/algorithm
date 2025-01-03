import sys
input=sys.stdin.readline

n=int(input())

a=list(map(int, input().split()))
res=int(1e9)
for i in range(n-1):
    target=a[i]
    start , end=i+1, n-1
    while True:
        if start>end:
            break
        mid=(start+end)//2
        cnt=target+a[mid]
        if abs(res)>abs(cnt):
            res=cnt
        if cnt<0:
            start=mid+1
        else:
            end=mid-1
print(res)