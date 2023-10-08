import sys
input=sys.stdin.readline

    
n=int(input())
a=list(map(int, input().split()))
a.sort()
res=0
result=0
for i in range(n):
    res+=a[i]
    result+=res
print(result)