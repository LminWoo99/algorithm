import sys, bisect
input=sys.stdin.readline

T=int(input())
n=int(input())
A=list(map(int, input().split()))
m=int(input())
B=list(map(int, input().split()))
answer=0

aSum=[]
bSum=[]

for i in range(n):
    s=A[i]
    aSum.append(s)
    for j in range(i+1, n):
        s+=A[j]
        aSum.append(s)
for i in range(m):
    s=B[i]
    bSum.append(s)
    for j in range(i+1, m):
        s+=B[j]
        bSum.append(s)

aSum.sort()
bSum.sort()
for i in range(len(aSum)):
    l=bisect.bisect_left(bSum, T-aSum[i])
    r=bisect.bisect_right(bSum, T-aSum[i])
    answer+=(r-l)    
print(answer)