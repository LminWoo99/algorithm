import sys
def DFS(l, sum):
    if l==n:
        if sum==(total-sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(l+1,sum+a[l])
        DFS(l+1, sum)
        
n=int(input())
a=list(map(int, input().split()))
total=sum(a)
DFS(0,0)
print("no")