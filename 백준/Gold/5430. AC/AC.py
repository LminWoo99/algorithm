import sys
input=sys.stdin.readline
from collections import deque
t=int(input())
i=0
while i<t:
    i+=1
    p=input().rstrip()
    n=int(input())
    arr = deque(input().rstrip()[1:-1].split(","))
    flag=True
    cnt=0
    if n==0:
        arr=[]
    for j in p:
        if j=='R':
            cnt+=1
        else:
            if len(arr)<1:
                flag=False
                break
            else:
                if cnt%2==1:
                    arr.pop()
                else:
                    arr.popleft()
    if cnt%2==1:
        arr.reverse()
    
    if not flag:
        print("error")
    else:
        print("[" + ",".join(arr) + "]")
    
