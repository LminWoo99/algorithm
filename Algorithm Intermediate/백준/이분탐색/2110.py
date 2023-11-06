import sys
input=sys.stdin.readline

n,c=map(int, input().split())
a=[]
for i in range(n):
    tmp=int(input())
    a.append(tmp)
a.sort()
result=0
start, end=1, a[n-1]

while start<=end:
        cnt=1
        est=a[0]
        mid=(start+end)//2
        for i in range(1, n):
            if a[i]-est>=mid:
                est=a[i]
                cnt+=1
        if cnt<c:
            end=mid-1
        else:
            result=mid
            start=mid+1
print(result)
            