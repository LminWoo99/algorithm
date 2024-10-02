import sys
from collections import deque
input=sys.stdin.readline
def BFS():
    dq=deque()
    dq.append((homeX, homeY))
    while dq:
        x,y=dq.popleft()
        if abs(x-rockX)+abs(y-rockY)<=1000:
            print("happy")
            return
        for i in range(n):
            if not visit[i]:
                xx,yy=store[i]
                if abs(x-xx)+abs(y-yy)<=1000:
                    visit[i]=1
                    dq.append((xx, yy))
    print("sad")
    return

t=int(input())
for _ in range(t):
    n=int(input())
    store=[]
    homeX, homeY=map(int, input().split())
    for _ in range(n):
        x,y=map(int, input().split())
        store.append((x,y))
    rockX, rockY=map(int, input().split())
    visit=[0]*(n+1)
    BFS()