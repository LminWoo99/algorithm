from collections import deque
import sys
n = int(sys.stdin.readline())
dq=deque()
for i in range(n):
    a=list(sys.stdin.readline().split())
    if a[0]=='push':
        dq.append(a[1])
    elif a[0]=='front':
        if len(dq)>0:
            print(dq[0])
        else:
            print(-1)
    elif a[0]=='back':
        if len(dq)>0:
            print(dq[-1])
        else:
            print(-1)
    elif a[0]=='size':
        print(len(dq))
    elif a[0]=='empty':
        if len(dq)==0:
            print(1)
        else:
            print(0)
    elif a[0]=='pop':
        if len(dq)>0:
            print(dq.popleft())
        else:
            print(-1)
