import sys
input=sys.stdin.readline
from collections import deque

def bfs():    
    global a,b,c,total, visit
    dq=deque()
    dq.append((a,b))
    visit[a][b]=True
    global result
    while dq:
        x,y= dq.popleft()
        z=total-x-y
        if x==y==z:
            print(1)
            return
        for a,b in (x,y), (y,z), (x,z):
            if a<b:
                b-=a
                a+=a
            elif a>b:
                a-=b
                b+=b
            else:
                continue
            c=total-a-b
            x=min(a,b,c)
            y=max(a,b,c)
            if not visit[x][y]:
                dq.append((x,y))
                visit[x][y]=True
    print(0)
a,b,c=map(int, input().split())
result=0
total=a+b+c
visit=[[False] * (total+1) for _ in range(total+1)]

if total % 3 !=0:
    print(0)
else:
    bfs()

