import sys, math

input=sys.stdin.readline

import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    x,y=map(int, input().split())
    ans=0
    if y-x<=3:
        print(y-x)
    else:
        tmp=int(math.sqrt(y-x))
        if y-x==tmp**2:
            print(2*tmp-1)
        else:
            print(2*tmp-1+math.ceil((y-x-tmp**2)/tmp))