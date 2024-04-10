import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int, input().split()))
a.sort()
res=0
for i in range(n):
    target=a[i]
    start=0
    end=len(a)-1
    while start<end:
        if a[start]+a[end]==target:
            if start==i:
                start+=1
            elif end==i:
                end-=1
            else:
                res+=1
                break
        elif a[start]+a[end]>target:
            end-=1
        else:
            start+=1
            
print(res)
                       