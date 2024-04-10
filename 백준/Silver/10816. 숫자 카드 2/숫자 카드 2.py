import sys
input=sys.stdin.readline
from collections import Counter
n=int(input())
a=list(map(int, input().split()))

count_a=Counter(a)
a=list(count_a)
a.sort()
m=int(input())
b=list(map(int, input().split()))
res=[]
for tmp in b:
    flag=False
    start=0
    end=len(a)-1
    while start<=end:
        mid=(start+end)//2
        if a[mid]==tmp:
            flag=True
            break
        elif a[mid]>tmp:
            end=mid-1
        else:
            start=mid+1
    if flag:
        res.append(count_a[tmp])
    else:
        res.append(0)
print(*res)