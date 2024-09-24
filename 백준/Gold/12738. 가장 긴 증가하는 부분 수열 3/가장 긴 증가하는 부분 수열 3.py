import sys
input=sys.stdin.readline

n=int(input())
A=list(map(int, input().split()))

temp=[A[0]]

for a in A[1:]:
    if temp[-1]<a:
        temp.append(a)
    else:
        left=0
        right=len(temp)
        while left<right:
            mid=(left+right)//2
            if temp[mid]<a:
                left=mid+1
            else:
                right=mid
        temp[right]=a
print(len(temp))