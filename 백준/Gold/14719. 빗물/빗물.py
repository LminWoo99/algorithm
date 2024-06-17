import sys
input=sys.stdin.readline
h,w=map(int, input().split())
a=list(map(int, input().split()))
res=0
for i in range(1, w-1):
    left=max(a[:i])
    right=max(a[i+1:])
    tmp=min(left, right)
    if a[i]<tmp:
        res+=(tmp-a[i])
print(res)