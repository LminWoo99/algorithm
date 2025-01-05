import sys
input=sys.stdin.readline

n,m=map(int, input().split())
a=[]
for _ in range(n):
    a.append(int(input()))
a.sort()
start, end=0,0
res=2*int(1e9)
while start<=end:
    if end>=n:
        break
    if abs(a[end]-a[start])>=m:
        res=min(abs(a[end]-a[start]), res)
        start+=1
    else:
        end+=1
print(res)