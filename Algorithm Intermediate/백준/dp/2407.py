import sys
input=sys.stdin.readline

n,m=map(int, input().split())
res=1
div=1
for i in range(n, n-m, -1):
    res*=i
for j in range(1, m+1):
    div*=j

print(res//div)
