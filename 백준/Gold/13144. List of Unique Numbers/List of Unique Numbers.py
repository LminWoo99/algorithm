import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int, input().split()))
res=0
check=set()
start=0
for end in range(n):
    while a[end] in check:
        check.remove(a[start])
        start+=1
    check.add(a[end])
    res+=(end-start+1)
print(res)