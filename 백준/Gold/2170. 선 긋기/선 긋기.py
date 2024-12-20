
import sys
input=sys.stdin.readline

n=int(input())
a=[]
for _ in range(n):
    x,y = map(int, input().split())
    a.append([x,y])
a.sort()
start , end= a[0][0] , a[0][1]
res=0
for i in range(1, len(a)):
    if a[i][0]<=end<a[i][1]:
        end=a[i][1]
    elif end<a[i][0]:
        res+=(end-start)
        start , end=a[i][0], a[i][1]
print(res+(end-start))