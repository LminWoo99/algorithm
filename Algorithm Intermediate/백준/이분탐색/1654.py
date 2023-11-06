import sys
input=sys.stdin.readline

k, n=map(int, input().split())
a=[]
for i in range(k):
    tmp=int(input())
    a.append(tmp)
start, end=1, max(a)
while start<=end:
    mid=(start+end)//2
    res=0
    for i in a:
        res+=i//mid
    if res>=n:
        start=mid+1
    else:
        end=mid-1    
print(end)