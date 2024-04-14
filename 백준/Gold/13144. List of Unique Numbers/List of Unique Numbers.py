import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int, input().split()))
res=0
visit=[0]*100001
start, end=0,0
while start<=end and end<n:
    if not visit[a[end]]:
        visit[a[end]]=1
        end+=1
        res+=end-start
    else:
        while visit[a[end]]:
            visit[a[start]]=0
            start+=1
    
print(res)
    
       