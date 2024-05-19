import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int, input().split()))

a.sort()
res=0
for i in range(n):
    start=0
    end=n-1
    target=a[i]
    while start<end:
        tmp=a[start]+a[end]
        if tmp<target:
            start+=1
        elif tmp==target:
            if start==i:
                start+=1
            elif end==i:
                end-=1
            else:
                res+=1
                break
        else:
            end-=1
print(res)