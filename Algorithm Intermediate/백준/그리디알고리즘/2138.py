import sys
input=sys.stdin.readline
def change(a,b):
    cnt=0
    a_copy=a[:]
    for i in range(1, n):
        if a_copy[i-1]==b[i-1]:
            continue
        cnt+=1
        for j in range(i-1, i+2):
            if j<n:
                a_copy[j]=1-a_copy[j]
    if a_copy==b:
        return cnt
    else:
        return 1e9
n=int(input())

current=list(map(int, input().rstrip()))
future=list(map(int, input().rstrip()))
res=change(current, future)

current[0]=1-current[0]
current[1]=1-current[1]
res=min(res, change(current, future)+1)
if res!=1e9:
    print(res)
else:
    print(-1)



            
    